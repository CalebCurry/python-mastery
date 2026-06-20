import psycopg
from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from pgvector.psycopg import register_vector


class Settings(BaseSettings):
    llm_base_url: HttpUrl = Field(init=False)
    llm_model: str = Field(init=False)
    embedder_base_url: HttpUrl = Field(init=False)
    embedder_model: str = Field(init=False)
    database_url: str = Field(init=False)
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()


def connect():
    conn = psycopg.connect(settings.database_url)
    register_vector(conn)
    return conn
