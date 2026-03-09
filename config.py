from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, HttpUrl, FilePath


class TestDataConfig(BaseModel):
    image_png_file: FilePath


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self):
        return str(self.url)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='allow',
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )
    test_data: TestDataConfig
    http_client: HTTPClientConfig

settings = Settings()
print(settings.model_dump().items())