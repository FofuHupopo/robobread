import os
from django.core.management import execute_from_command_line

from .utils import load_env


def main():
    load_env()
    
    from django.contrib.auth.models import User

    execute_from_command_line(['manage.py', 'migrate'])
    
    username = os.getenv("ADMIN_USERNAME")
    email = os.getenv("ADMIN_EMAIL")
    password = os.getenv("ADMIN_PASSWORD")
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(username, email, password)
        print(f'Superuser {username} created successfully!')
    else:
        print(f'Superuser {username} already exists.')
