from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str

    app_host: str = "0.0.0.0"
    app_port: int = 5000

    debug: bool = False
    secret_key: str = "changeme"

    class Config:
        env_file = ".env"
        env_prefix = ""
        extra = "ignore"


settings = Settings()
