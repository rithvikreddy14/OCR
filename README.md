# Patient Assessment Form OCR Processor

A Python-based solution to automate extraction of patient assessment data from scanned forms (printed/handwritten) using OCR, convert it to structured JSON, and store in a PostgreSQL database.

## Features

- 📷 OCR processing using Tesseract with image preprocessing
- 🗂️ Structured JSON output matching medical form requirements
- 🗄️ PostgreSQL database integration
- 🔍 Regex-based data parsing for key medical fields

## Prerequisites

1. **Tesseract OCR**  
   Install from [official docs](https://github.com/tesseract-ocr/tesseract)  
   Add to system PATH for Python access

2. **PostgreSQL**  
   [Install guide](https://www.postgresql.org/download/)

3. **Python 3.8+**  
   Required packages in `requirements.txt`

## Installation

1. Clone repository:
'''git clone https://github.com/rithvikreddy14/patient-form-ocr.git'''

2.Install dependencies:
'''pip install -r requirements.txt'''
3.Database setup:
'''psql -U postgres -f schema.sql'''

##Usage

1.Place form images in project root (e.g., sample_form.jpg)
2.Run OCR processor:
'''python ocr_script.py'''
