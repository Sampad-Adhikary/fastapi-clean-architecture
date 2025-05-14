from sqlalchemy import Column, Integer, String
from app.db.base import Base

class CSVData(Base):
    __tablename__ = "csv_data"

    id = Column(Integer, primary_key=True, index=True)
    column1 = Column(String, index=True)
    column2 = Column(String, index=True)
    # Add more columns as needed based on the CSV structure
