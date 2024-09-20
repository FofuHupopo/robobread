from pathlib import Path

from .utils import getenv


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv("SECRET_KEY")

DEBUG = getenv("DEBUG") == "true"

VENDING_MACHINES_PROTOCOL = getenv("VENDING_MACHINES_PROTOCOL")

ALLOWED_HOSTS = [
    "*"
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # REST
    'rest_framework',
    'corsheaders',
    'drf_spectacular',

    # API
    'api.vending_machines',
    'api.packing',
    'api.products',

    # Frontend
    'frontend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'api.middlewares.ServiceResponseExceptionMiddleware',
    'api.middlewares.NoObjectExceptionMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db' / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "static/"


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / "media/"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOWED_ORIGINS = []

CSRF_TRUSTED_ORIGINS = []

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "POST",
    "PUT",
]


TWENTY_MEGABYTES = 20 * 1024 * 1024

DATA_UPLOAD_MAX_MEMORY_SIZE = TWENTY_MEGABYTES
FILE_UPLOAD_MAX_MEMORY_SIZE = TWENTY_MEGABYTES


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Accounting API',
    'DESCRIPTION': 'API для сервиса учета товаров и затаривания по всем торговым автоматам.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'TAGS': [
        {'name': 'Затаривание', 'description': 'Затаривания каждого автомата'},
        {'name': 'Синхронизация', 'description': 'Синхроназация с автоматом (Для проверки в сети ли он)'},
        {'name': 'Категории автомата', 'description': 'Управление категориями в автомате'},
        {'name': 'Ячейки автомата', 'description': 'Управление ячейками в автомате'},
        {'name': 'Товары автомата', 'description': 'Управление товарами в автомате'},
    ],
}
