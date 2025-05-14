from fastapi import APIRouter, UploadFile, File
import pandas as pd
from app.services.csv_service import process_csv

router = APIRouter()

@router.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(pd.compat.StringIO(contents.decode('utf-8')))
    await process_csv(df)
    return {"message": "CSV file processed successfully."}