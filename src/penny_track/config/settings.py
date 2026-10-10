from pydantic_settings import BaseSettings, SettingsConfigDict

from functools import lru_cache


class Settings(BaseSettings):
    database_url: str
    postgres_user: str = "postgres"
    postgres_password: str
    postgres_db: str = "penny_track"
    postgres_port: int = 5432
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )
    
@lru_cache # Permite que a função reutilize a primeira instância após a primeira execução sem precisar reler o .env toda hora
def get_settings() -> Settings:
    return Settings()

settings = get_settings()