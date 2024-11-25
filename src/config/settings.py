from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "ACA Certification System"
    
    # SambaNova Configuration
    SAMBANOVA_API_KEY: str = "9b87ae98-63f3-4d5b-8d25-77c27690beb4"
    SAMBANOVA_BASE_URL: str = "https://api.sambanova.ai/v1"
    SAMBANOVA_MODEL: str = "Meta-Llama-3.1-8B-Instruct"
    
    # Database Configuration
    DATABASE_URL: str
    
    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    class Config:
        env_file = ".env"

settings = Settings()