import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_csv():
    with open("tests/test_data.csv", "rb") as csv_file:
        response = client.post("/upload-csv", files={"file": csv_file})
    
    assert response.status_code == 200
    assert response.json() == {"message": "CSV file uploaded successfully."}