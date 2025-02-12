
# Patient Assessment Form OCR Processor

A Python-based solution to automate extraction of patient assessment data from scanned forms (printed/handwritten) using OCR, convert it to structured JSON, and store it in a PostgreSQL database.



## Features

- 📷 **OCR Processing**: Uses Tesseract OCR with image preprocessing (grayscale, thresholding) for accurate text extraction.
- 🗂️ **Structured JSON Output**: Conforms to medical form requirements, including patient details, treatment data, and symptom ratings.
- 🗄️ **Database Integration**: Stores extracted data in a PostgreSQL database with a well-defined schema.
- 🔍 **Regex-Based Parsing**: Extracts key fields like patient name, DOB, treatment details, and symptom ratings.
## Prerequisites
Before running the project, ensure the following are installed:

1. **Tesseract OCR**  
   Install from [official docs](https://github.com/tesseract-ocr/tesseract).  
   Add Tesseract to your system PATH for Python access.

2. **PostgreSQL**  
   Download and install from the [official website](https://www.postgresql.org/download/).

3. **Python 3.8+**  
   Ensure Python is installed. Install required packages using `requirements.txt`.
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rithvikreddy14/patient-form-ocr.git
   cd patient-form-oc
2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
3. Set up the PostgreSQL database:
    ```bash
    CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE
    );
    
    CREATE TABLE forms_data (
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(id),
    form_json JSONB,
    created_at TIMESTAMP DEFAULT NOW()
    );

## Project Structure
```bash
├── ocr_processor.py       # Main OCR processing script
├── requirements.txt       # Python dependencies
├── README.md              # This documentation
└── sample_form.jpg        # Sample form image for testing
```
## Limitations

✍️ Handwriting Recognition: Accuracy depends on image quality and handwriting clarity.

📄 Form Structure: Assumes the form structure matches the provided samples.

⚠️ Regex Parsing: Basic regex is used for field extraction; may need enhancement for complex forms.
## Contributing

1. Fork the repository.

2. Create a new branch (git checkout -b feature/improvement).

3. Commit your changes (git commit -m 'Add some feature').

4. Push to the branch (git push origin feature/improvement).

5. Open a Pull Request.
