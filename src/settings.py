from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_host: str = '0.0.0.0'
    server_port: int = 8000
    reload: bool = False

    access_key: str = None


settings = Settings(
    _env_file='./.env',
    _env_file_encoding='UTF-8'
)
