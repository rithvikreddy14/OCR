import psycopg2
from psycopg2.extras import execute_values

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="patient_db",
            user="postgres",
            password="password",
            host="localhost"
        )
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                dob DATE
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS forms_data (
                id SERIAL PRIMARY KEY,
                patient_id INT REFERENCES patients(id),
                form_json JSONB,
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)
        self.conn.commit()

    def insert_patient(self, name, dob):
        self.cur.execute(
            "INSERT INTO patients (name, dob) VALUES (%s, %s) RETURNING id",
            (name, dob)
        )
        patient_id = self.cur.fetchone()[0]
        self.conn.commit()
        return patient_id

    def insert_form(self, patient_id, form_data):
        self.cur.execute(
            "INSERT INTO forms_data (patient_id, form_json) VALUES (%s, %s)",
            (patient_id, json.dumps(form_data))
        )
        self.conn.commit()