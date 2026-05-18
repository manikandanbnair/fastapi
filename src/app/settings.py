from pydantic_settings import BaseSettings, SettingsConfigDict

class PostgresSettings(BaseSettings):
    host: str 
    port: int 
    user: str 
    password: str
    db_name: str 
    model_config = SettingsConfigDict(env_prefix="POSTGRES_")

class Settings(BaseSettings):

    env: str = 'development'

    db: PostgresSettings = PostgresSettings()
