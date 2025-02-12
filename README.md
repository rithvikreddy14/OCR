# Patient Assessment Form OCR Processor

A Python-based solution to automate extraction of patient assessment data from scanned forms (printed/handwritten) using OCR, convert it to structured JSON, and store it in a PostgreSQL database.

---

## Features

- 📷 **OCR Processing**: Uses Tesseract OCR with image preprocessing (grayscale, thresholding) for accurate text extraction.
- 🗂️ **Structured JSON Output**: Conforms to medical form requirements, including patient details, treatment data, and symptom ratings.
- 🗄️ **Database Integration**: Stores extracted data in a PostgreSQL database with a well-defined schema.
- 🔍 **Regex-Based Parsing**: Extracts key fields like patient name, DOB, treatment details, and symptom ratings.

---

## Prerequisites

Before running the project, ensure the following are installed:

1. **Tesseract OCR**  
   Install from [official docs](https://github.com/tesseract-ocr/tesseract).  
   Add Tesseract to your system PATH for Python access.

2. **PostgreSQL**  
   Download and install from the [official website](https://www.postgresql.org/download/).

3. **Python 3.8+**  
   Ensure Python is installed. Install required packages using `requirements.txt`.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/patient-form-ocr.git
   cd patient-form-ocr
