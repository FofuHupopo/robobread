"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()


def sync_all():
    from api.synchronizer import SyncableModel

    for model in SyncableModel.__subclasses__():
        for obj in model.objects.all():
            obj.sync()


sync_all()
