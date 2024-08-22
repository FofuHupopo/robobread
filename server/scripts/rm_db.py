from pathlib import Path
from django.conf import settings

from .utils import load_env


def main():
    load_env()

    db_path = Path(settings.DATABASES["default"]["NAME"])
    db_path.unlink()

    print("Database deleted!")


if __name__ == "__main__":
    main()
