import os
from pathlib import Path

import environ

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_DIR = Path(__file__).resolve().parent
BASE_DIR = PROJECT_DIR.parent
env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = env.bool('DEBUG', False)
SECRET_KEY = env.str('SECRET_KEY', 'the-best-pass')
ALLOWED_HOSTS = env.str("ALLOWED_HOSTS").split(",")

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # frameworks
    'debug_toolbar',
    'rest_framework',
    'drf_yasg',
    # project apps
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
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

# Database
DATABASES = {
    'default': {
        'ENGINE': env.str('SQL_ENGINE', 'db_engine'),
        'NAME': env.str('SQL_DATABASE', 'db_name'),
        'USER': env.str('SQL_USER', 'db_username'),
        'PASSWORD': env.str('SQL_PASSWORD', 'db_pass'),
        'HOST': env.str('SQL_HOST', 'db_host'),
        'PORT': env.str('SQL_PORT', '5000'),
    }
}

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

# Internationalization
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '%(levelname)-6s %(asctime)-6s %(name)s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_DIR, "logs", "info.log"),
            'formatter': 'file',
            'maxBytes': 1024 * 1024 * 1,  # 1 MB,
            'backupCount': 5,
            'encoding': 'utf-8',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.server': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': True,
        },
        'django': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': True,
        },
    },
}

if DEBUG:
    # If DEBUG is True to write log to console, else write to file.
    LOGGING['loggers'] = {
        'django.server': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        }
    }

# DRF settings
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '50/hour',
        'anon': '30/hour',
    },
}
