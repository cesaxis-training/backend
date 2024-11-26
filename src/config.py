import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_ENV = os.getenv("FLASK_ENV")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

    @staticmethod
    def validate():
        missing_vars = [var for var in ["FLASK_ENV", "MYSQL_HOST", "MYSQL_USER", "MYSQL_PASSWORD", "MYSQL_DATABASE"] if not os.getenv(var)]
        if missing_vars:
            raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

# Validate configuration
Config.validate()
