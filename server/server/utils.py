import os


class MissingEnvironmentVariable(Exception):
    pass


def getenv(key: str) -> str:
    try:
        return os.environ[key]
    except KeyError:
        raise MissingEnvironmentVariable(f"{key} does not exist at .env file")
