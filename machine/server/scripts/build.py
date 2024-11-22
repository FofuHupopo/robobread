import os
from django.core.management import execute_from_command_line

from .utils import load_env


def main():
    load_env()

    host = "0.0.0.0"
    port = os.getenv('PORT', 8000)

    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    execute_from_command_line(['manage.py', 'migrate'])
    execute_from_command_line(['manage.py', 'runserver', f"{host}:{port}"])


if __name__ == "__main__":
    main()
