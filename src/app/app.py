import os
import sys
import streamlit as st
import json

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.utils.pdf_utils import extract_text_from_pdf
from src.utils.image_utils import extract_text_from_image
from src.core.cv_extractor import CVExtractor

# Configuration
MODEL_NAME = os.getenv("MODEL_NAME", "mistralai/Mistral-Nemo-Instruct-2407")

st.set_page_config(page_title="AI CV Parser", page_icon="📄", layout="wide")

# Custom CSS for a professional look
st.markdown("""
<style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #4A90E2; color: white; }
    .upload-section { padding: 2rem; border: 2px dashed #4A90E2; border-radius: 10px; background-color: white; }
    .result-card { padding: 1.5rem; border-radius: 10px; background-color: white; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def get_extractor():
    return CVExtractor(model_name=MODEL_NAME)

def main():
    st.title("📄 AI-Powered CV Parser")
    st.markdown("Extract structured data from resumes using state-of-the-art LLMs.")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Upload Resume")
        uploaded_file = st.file_uploader("Choose a PDF or Image file", type=["pdf", "png", "jpg", "jpeg"])
        
        if uploaded_file:
            file_bytes = uploaded_file.read()
            
            if st.button("Extract Information"):
                with st.spinner("Processing document..."):
                    try:
                        # Extract text based on file type
                        if uploaded_file.type == "application/pdf":
                            raw_text = extract_text_from_pdf(file_bytes)
                        else:
                            raw_text = extract_text_from_image(file_bytes)

                        if not raw_text.strip():
                            st.error("Could not extract text from the document. Please try another file.")
                            return

                        # Use the real LLM extractor
                        extractor = get_extractor()
                        structured_data = extractor.parse(raw_text)
                        
                        st.session_state['parsed_data'] = structured_data
                        st.success("Extraction complete!")
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")

    with col2:
        st.subheader("Extracted Data")
        if 'parsed_data' in st.session_state:
            data = st.session_state['parsed_data']
            
            st.markdown("<div class='result-card'>", unsafe_allow_html=True)
            st.json(data)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Download button for JSON
            json_string = json.dumps(data, indent=4)
            st.download_button(
                label="Download JSON",
                data=json_string,
                file_name="extracted_cv.json",
                mime="application/json"
            )
        else:
            st.info("Upload a CV and click 'Extract Information' to see the results.")

if __name__ == "__main__":
    main()
