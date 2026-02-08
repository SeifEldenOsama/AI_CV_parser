# AI-Powered CV Parser 📄

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Model: Mistral-Nemo](https://img.shields.io/badge/Model-Mistral--Nemo-orange.svg)](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407)

A professional-grade tool designed to automate the extraction of structured data from resumes (CVs) using Large Language Models (LLMs). This application converts unstructured PDF or image-based resumes into standardized JSON format, streamlining recruitment and HR workflows.

## 🌟 Key Features

- **LLM-Powered Extraction**: Leverages `Mistral-Nemo-Instruct-2407` for intelligent text understanding and data extraction.
- **Structured Output**: Guarantees clean, predictable JSON output using LangChain's structured output parsers.
- **Multi-Format Support**: Seamlessly processes both PDF documents and image-based resumes (OCR).
- **Interactive Dashboard**: A sleek Streamlit interface for real-time file uploads and result visualization.
- **Professional Architecture**: Modular code structure following industry best practices for scalability and maintenance.

## 📁 Project Structure

```text
AI_CV_parser/
├── assets/                 # Media assets and project presentations
├── data/                   # Sample CVs for testing
├── docs/                   # Detailed documentation and guides
├── notebooks/              # Jupyter notebooks for experimentation
├── src/                    # Source code
│   ├── app/                # Streamlit application logic
│   ├── core/               # Core LLM extraction logic
│   └── utils/              # Document processing utilities
├── tests/                  # Unit tests
├── LICENSE                 # MIT License
├── README.md               # Project overview
└── requirements.txt        # Project dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- CUDA-enabled GPU (recommended for LLM inference)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SeifEldenOsama/AI_CV_parser.git
   cd AI_CV_parser
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Running the Web Application
To start the Streamlit interface:
```bash
streamlit run src/app/app.py
```

## 📊 Extracted Data Schema

The parser extracts the following fields into a structured JSON object:
- `full_name`: Candidate's full name.
- `email`: Primary contact email.
- `education`: List of degrees, institutions, and dates.
- `skills`: Comprehensive list of technical and soft skills.
- `experience`: Detailed work history including roles and companies.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---
