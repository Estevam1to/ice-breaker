from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    ANTROPIC_API_KEY: str
    PROXY_CURL_API_KEY: str
    PROXY_CURL_API_URL: str


settings = Settings()


if __name__ == "__main__":
    print(settings.model_dump())
