from pydantic import BaseSettings, Field, PostgresDsn

class Settings(BaseSettings):
    APP_NAME: str = "WorkoutAPI"
    ENV: str = "development"
    POSTGRES_USER: str = Field("workout", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field("workout", env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field("workout_db", env="POSTGRES_DB")
    POSTGRES_HOST: str = Field("db", env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")
    POSTGRES_DSN: PostgresDsn | str = Field(
        None, env="POSTGRES_DSN"
    )  # accept full DSN or compose
    DATABASE_URL: str | None = Field(None, env="DATABASE_URL")

    def __init__(self, **values):
        super().__init__(**values)
        if not self.POSTGRES_DSN:
            self.POSTGRES_DSN = f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env"

settings = Settings()
