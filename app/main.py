from fastapi import FastAPI
from app.api.endpoints.upload_csv import router as upload_csv_router

app = FastAPI()

app.include_router(upload_csv_router)