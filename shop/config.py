from pydantic_settings import BaseSettings, SettingsConfigDict
import asyncio

class Settings(BaseSettings):
    db_url: str
    kafka_topic: str
    kafka_bootstrap_server: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

loop = asyncio.get_event_loop()
