import cv2
import pytesseract
import re
import json
from database import Database

class OCRProcessor:
    def __init__(self):
        self.db = Database()
        
    def preprocess_image(self, image_path):
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return thresh

    def extract_text(self, image_path):
        processed_img = self.preprocess_image(image_path)
        text = pytesseract.image_to_string(processed_img)
        return text

    def parse_patient_details(self, text):
        details = {}
        details["patient_name"] = re.search(r"Patient Name : (.*)", text).group(1).strip()
        details["dob"] = re.search(r"DOB : (.*)", text).group(1).strip()
        return details

    def parse_treatment_details(self, text):
        treatment = {}
        injection = re.search(r"INJECTION : (YES|NO)", text)
        exercise = re.search(r"Exercise Therapy : (YES|NO)", text)
        treatment["injection"] = injection.group(1) if injection else "No"
        treatment["exercise_therapy"] = exercise.group(1) if exercise else "No"
        treatment["date"] = re.search(r"Date : (.*?)\s+MA Initials", text).group(1).strip()
        return treatment

    def parse_ratings(self, text, pattern, scale_max):
        ratings = {}
        for line in text.split('\n'):
            for activity in pattern:
                if activity in line:
                    match = re.search(rf"{activity}.*?(\d+)", line)
                    if match:
                        ratings[activity.lower().replace(" ", "_")] = int(match.group(1))
        return ratings

    def parse_pain_symptoms(self, text):
        symptoms = {}
        pain_line = re.search(r"Pain:.*?(\d+)", text)
        numbness_line = re.search(r"Numbness:.*?(\d+)", text)
        tingling_line = re.search(r"Tingling:.*?(\d+)", text)
        burning_line = re.search(r"Burning:.*?(\d+)", text)
        tightness_line = re.search(r"Tightness:.*?(\d+)", text)
        
        symptoms["pain"] = int(pain_line.group(1)) if pain_line else 0
        symptoms["numbness"] = int(numbness_line.group(1)) if numbness_line else 0
        symptoms["tingling"] = int(tingling_line.group(1)) if tingling_line else 0
        symptoms["burning"] = int(burning_line.group(1)) if burning_line else 0
        symptoms["tightness"] = int(tightness_line.group(1)) if tightness_line else 0
        return symptoms

    def process_form(self, image_path):
        text = self.extract_text(image_path)
        
        data = {}
        data.update(self.parse_patient_details(text))
        data.update(self.parse_treatment_details(text))
        
        # Difficulty Ratings (0-5)
        activities = [
            "Bending or Stooping", "Putting on shoes", "Sleeping",
            "Standing for an hour", "Going up or down a flight of stairs",
            "Walking through a store", "Driving for an hour", "Preparing a meal",
            "Yard work", "Picking up items off the floor"
        ]
        data["difficulty_ratings"] = self.parse_ratings(text, activities, 5)
        
        # Patient Changes
        changes = {}
        changes["since_last_treatment"] = re.search(r"since last treatment:\s*(.*?)\n", text, re.IGNORECASE).group(1).strip()
        changes["since_start_of_treatment"] = re.search(r"since the start of treatment:\s*(.*?)\n", text, re.IGNORECASE).group(1).strip()
        changes["last_3_days"] = re.search(r"last three days \(good/bad\):\s*(.*?)\n", text, re.IGNORECASE).group(1).strip()
        data["patient_changes"] = changes
        
        # Pain Symptoms
        data["pain_symptoms"] = self.parse_pain_symptoms(text)
        
        # MA Data
        ma_data = {}
        ma_fields = {
            "blood_pressure": r"Blood Pressure: (.*?)\s",
            "hr": r"HR: (\d+)",
            "weight": r"Weight: (\d+)",
            "height": r"Height: (.*?)\s",
            "spo2": r"SpO2: (\d+)",
            "temperature": r"Temperature: (.*?)\s",
            "blood_glucose": r"Blood Glucose: (\d+)",
            "respirations": r"Respirations: (\d+)"
        }
        for key, pattern in ma_fields.items():
            match = re.search(pattern, text)
            ma_data[key] = match.group(1).strip() if match else None
        data["medical_assistant_data"] = ma_data
        
        # Save to DB
        patient_id = self.db.insert_patient(data["patient_name"], data["dob"])
        self.db.insert_form(patient_id, data)
        
        return json.dumps(data, indent=2)

if __name__ == "__main__":
    processor = OCRProcessor()
    result = processor.process_form("sample_form.jpg")
    print(result)