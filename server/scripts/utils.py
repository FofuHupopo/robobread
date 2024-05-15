import os
from pathlib import Path
from dotenv import load_dotenv


def load_env():
    if "DB_PASSWORD" in os.environ:
        del os.environ["DB_PASSWORD"]

    DOTENV_PATH = Path(__file__).resolve().parent.parent / '.env'
    load_dotenv(DOTENV_PATH)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'server.settings')
