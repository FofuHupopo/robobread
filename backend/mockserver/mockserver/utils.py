import os
import json

from pathlib import Path



DB_PATH = Path(__file__).absolute().parent.parent / "db"


class MissingEnvironmentVariable(Exception):
    pass


def getenv(key: str) -> str:
    try:
        return os.environ[key]
    except KeyError:
        raise MissingEnvironmentVariable(f"{key} does not exist at .env file")


def read_json(file_name: str) -> dict:
    with open(DB_PATH / file_name, 'r') as f:
        return json.load(f)
