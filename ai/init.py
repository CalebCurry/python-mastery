from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    llm_base_url: HttpUrl = Field(init=False)
    llm_model: str = Field(init=False)
    embedder_base_url: HttpUrl = Field(init=False)
    embedder_model: str = Field(init=False)
    database_url: str = Field(init=False)
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()
