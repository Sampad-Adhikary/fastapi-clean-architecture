from pydantic import BaseModel
from typing import List

class CSVData(BaseModel):
    column1: str
    column2: str
    column3: str
    # Add more fields as necessary based on the CSV structure

class CSVDataList(BaseModel):
    data: List[CSVData]