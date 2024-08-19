from pathlib import Path
from django.core.management import execute_from_command_line
from django.conf import settings

from .utils import load_env
from .migrate import main as migrate
from .createsuperuser import main as createsuperuser


def main():
    load_env()

    db_path = Path(settings.DATABASES["default"]["NAME"])
    db_path.unlink()

    migrate()
    createsuperuser()
    execute_from_command_line(['manage.py', 'fill_db'])
    print("Database created!")
