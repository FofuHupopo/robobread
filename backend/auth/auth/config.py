import os


class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")  # Секретный ключ для JWT
    ALGORITHM: str = "HS256"
    TOKEN_EXPIRY_MINUTES: int = 30  # Время жизни токена в минутах


settings = Settings()
