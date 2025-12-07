from transformers import AutoModelForCausalLM, AutoTokenizer
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate
import torch
import re
from pypdf import PdfReader

class CVExtractor:

    def __init__(self, model_name="mistralai/Mistral-Nemo-Instruct-2407"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        self._setup_schema()

    def _setup_schema(self):
        self.schemas = [
            ResponseSchema(name="full_name", description="Candidate full name."),
            ResponseSchema(name="email", description="Candidate email."),
            ResponseSchema(name="education", description="Education entries."),
            ResponseSchema(name="skills", description="Skills list."),
            ResponseSchema(name="experience", description="Work experience.")
        ]

        self.parser = StructuredOutputParser.from_response_schemas(self.schemas)
        self.format_instructions = self.parser.get_format_instructions()

    def extract_json_block(self, text):
        matches = re.findall(r'```json\s*(.*?)\s*```', text, re.DOTALL)
        return matches[-1] if matches else "{}"

    def generate(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            **inputs,
            max_length=5000,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7,
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def parse(self, text):
        template = """
        You are a resume parser. Extract structured JSON:
        {format_instructions}

        Resume Text:
        "{text}"
        """

        prompt = PromptTemplate(
            template=template,
            input_variables=["text", "format_instructions"]
        ).format(text=text, format_instructions=self.format_instructions)

        raw = self.generate(prompt)
        json_block = self.extract_json_block(raw)

        return self.parser.parse(json_block)
