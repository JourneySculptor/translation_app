from pydantic import BaseSettings

class Settings(BaseSettings):
    authjwt_secret_key: str = "s3cUr3JWTK3yF0rT0k3n2025"

settings = Settings()
