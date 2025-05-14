# File: /fastapi-clean-architecture/fastapi-clean-architecture/app/services/csv_service.py

from typing import List
import pandas as pd
from app.db.session import get_db
from app.models.csv_data import CsvData
from sqlalchemy.orm import Session

def process_csv(file_path: str) -> List[dict]:
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')

def save_csv_data_to_db(csv_data: List[dict], db: Session):
    for record in csv_data:
        csv_record = CsvData(**record)
        db.add(csv_record)
    db.commit()

def handle_csv_upload(file_path: str):
    db = get_db()
    csv_data = process_csv(file_path)
    save_csv_data_to_db(csv_data, db)