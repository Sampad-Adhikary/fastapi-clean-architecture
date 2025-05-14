import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
    CSV_UPLOAD_FOLDER = os.getenv("CSV_UPLOAD_FOLDER", "./uploads")
    MAX_CSV_FILE_SIZE = int(os.getenv("MAX_CSV_FILE_SIZE", 10 * 1024 * 1024))  # 10 MB
    ALLOWED_EXTENSIONS = {'csv'}

config = Config()