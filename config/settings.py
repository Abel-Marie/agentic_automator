import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = "gemini-1.5-flash" # Free tier model
    TIMEOUT_SECONDS = 30
    MAX_RETRIES = 3
    DB_PATH = "./chroma_db"

settings = Settings()