from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI-Powered Customer Complaint Management System"
    VERSION: str = "1.0.0"
    
    DATABASE_URL: str
    GROQ_API_KEY: str
    
    # Optional settings
    LOG_LEVEL: str = "INFO"
    UPLOAD_DIRECTORY: str = "uploads"
    MAX_FILE_SIZE: int = 10485760 # 10MB
    ENVIRONMENT: str = "development"
    SECRET_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
