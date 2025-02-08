import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    database_url: str = os.getenv("DATABASE_URL")
    secret_key: str = os.getenv("SECRET_KEY")
    hash_algorithm: str = os.getenv("HASH_ALGORITHM")
    access_token_expires: int = int(os.getenv("ACCESS_TOKEN_EXPIRES"))
    refresh_token_expires: int = int(os.getenv("REFRESH_TOKEN_EXPIRES"))

settings = Settings()