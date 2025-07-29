# from pydantic_settings import BaseSettings
# from typing import Optional

# class Settings(BaseSettings):
#     """Application settings"""
    
#     # API Settings
#     api_v1_str: str = "/api/v1"
#     project_name: str = "FastAPI Application"
    
#     # Database Settings
#     database_url: Optional[str] = None
    
#     # Security Settings
#     secret_key: str = "your-secret-key-here"
#     algorithm: str = "HS256"
#     access_token_expire_minutes: int = 30
    
#     # CORS Settings
#     allowed_hosts: list = ["http://localhost:3000", "http://localhost:8501", "http://127.0.0.1:8501"]
    
#     class Config:
#         env_file = ".env"

# # Create settings instance
# settings = Settings() 