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
    'api.products',
    'api.payment',
    'api.orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

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

WSGI_APPLICATION = 'server.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db' / 'db.sqlite3',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': getenv('DB_NAME'),
    #     'USER': getenv('DB_USER'),
    #     'PASSWORD': getenv('DB_PASSWORD'),
    #     'HOST': getenv('DB_HOST'),
    #     'PORT': getenv('DB_PORT'),
    # },
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

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "static/"

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / "media/"


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


DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 20  # 20 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 20  # 20 MB


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


TINKOFF_PAYMENTS_CONFIG = {
    'TAXATION': 'usn_income',
    'ITEM_TAX': 'none',
    'TERMINAL_KEY': getenv("TERMINAL_KEY"),
    'SECRET_KEY': getenv("SECRET_KEY"),
    'SUCCESS_URL': '',
    'FAIL_URL': '',
    'RECEIPT_EMAIL': getenv('RECEIPT_EMAIL'),
    'RECEIPT_PHONE': getenv('RECEIPT_PHONE'),
}
