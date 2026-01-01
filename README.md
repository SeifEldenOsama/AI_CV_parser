# AI CV Parser: Structured Resume Data Extraction with LLMs

## Project Overview

The **AI CV Parser** is a powerful application designed to automate the process of extracting key information from resumes (CVs) and converting it into a structured JSON format. Leveraging the capabilities of Large Language Models (LLMs) and advanced natural language processing techniques, this tool significantly streamlines recruitment and HR workflows by providing accurate, standardized data from unstructured documents.

The system is built around a robust LLM, specifically instructed and constrained to output data according to a predefined schema, ensuring reliability and ease of integration with other systems.

## Key Features

*   **LLM-Powered Extraction:** Utilizes a state-of-the-art Causal Language Model (e.g., `mistralai/Mistral-Nemo-Instruct-2407`) for intelligent text parsing and data extraction.
*   **Structured Output Guarantee:** Employs **LangChain's Structured Output Parser** to enforce a clean, predictable JSON output format, minimizing parsing errors and ensuring data quality.
*   **Comprehensive Data Fields:** Extracts essential candidate information, including Full Name, Email, Education, Skills, and Work Experience.
*   **PDF Processing:** Integrates **PyPDF** utilities to seamlessly handle and extract text content from PDF resume files.
*   **Interactive Web Interface:** A user-friendly application built with **Streamlit** allows users to upload CVs and view the extracted structured data in real-time.
*   **Deployment Ready:** Includes server-side components with **Pyngrok** integration for easy public deployment and testing.

## Technical Specifications

The project relies on a modern and efficient Python-based technology stack:

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Core Model** | Mistral-Nemo-Instruct-2407 | The LLM used for text understanding and structured data generation. |
| **LLM Framework** | Hugging Face `transformers` | For loading and managing the Causal Language Model. |
| **NLP Utility** | `langchain` | Provides structured output parsing and prompt templating capabilities. |
| **Document Processing** | `PyPDF` | Extracts raw text content from PDF resume files. |
| **Web Application** | `Streamlit` | Hosts the interactive user interface for file upload and result display. |
| **Deployment** | `pyngrok` | Facilitates public exposure of the local Streamlit application. |
| **Data Format** | JSON | The standardized output format for extracted CV data. |

### Extracted Data Schema

The parser is configured to extract the following fields into a structured JSON object:

| Field Name | Description | Data Type |
| :--- | :--- | :--- |
| `full_name` | The candidate's full name. | String |
| `email` | The candidate's primary email address. | String |
| `education` | A list of education entries (degrees, institutions, dates). | List of Strings/Objects |
| `skills` | A comprehensive list of technical and soft skills. | List of Strings |
| `experience` | A list of work experience entries (roles, companies, duration). | List of Strings/Objects |

## Repository Structure

The project is organized into logical directories for clear separation of concerns:

```
.
├── application/                # Contains the Streamlit web application script (app.py).
├── models/                     # Core logic for the LLM-based CV extraction (cv_extractor.py).
├── notebooks/                  # Jupyter Notebooks used for development and experimentation.
├── presentation/               # Project presentation and documentation materials.
├── server/                     # Scripts for server-side deployment and ngrok integration.
├── utils/                      # Utility functions, including PDF text extraction (pdf_utils.py).
└── requirements.txt            # List of all necessary Python dependencies.
```

## Getting Started

### Prerequisites

*   Python 3.x
*   Access to a machine with sufficient resources (GPU recommended for LLM inference).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/SeifEldenOsama/AI_CV_parser.git
    cd AI_CV_parser
    ```

2.  **Install dependencies:**
    Install all required packages listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

The application is run via the Streamlit interface.

1.  **Set up the server (Optional but Recommended):**
    If you plan to expose the application publicly, configure your ngrok authentication token.
    ```bash
    # Set your ngrok auth token if using the server/ngrok_server.py script
    export NGROK_AUTH_TOKEN="YOUR_NGROK_AUTH_TOKEN"
    ```

2.  **Start the Streamlit App:**
    ```bash
    streamlit run application/app.py
    ```

The application will launch in your browser, allowing you to upload a PDF CV and receive the structured JSON output.

---
