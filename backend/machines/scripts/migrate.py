from django.core.management import execute_from_command_line

from .utils import load_env


def main():
    load_env()

    execute_from_command_line(['manage.py', 'makemigrations'])
    execute_from_command_line(['manage.py', 'migrate'])


if __name__ == "__main__":
    main()
