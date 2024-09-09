from pathlib import Path

from .utils import getenv


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv("SECRET_KEY")

DEBUG = getenv("DEBUG") == "true"

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
    'api.core',
    'api.statistics',

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
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
        'NAME': BASE_DIR / 'db/db.sqlite3',
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

STATICFILES_DIRS = [
    BASE_DIR / 'frontend/static',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://localhost",
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://localhost",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'filename',
    "Content-Disposition",
    'name',
    "boundary",
    "Set-Cookie",
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
    'TITLE': 'Analytics API',
    'DESCRIPTION': 'API для аналитики продаж и товарного остатка',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'TAGS': [
        {'name': 'Торговые автоматы', 'description': 'CRUD по торговым автоматам (update происходит на стороне автомата)'},
        {'name': 'Статистика продаж', 'description': 'Статистика продаж по всем автоматам вместе'},
        {'name': 'Товарный остаток', 'description': 'Получение информации по товарному остатку в каждом автомате'},
    ],
}
