"""
Django settings for ibasco_league project.
"""

from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------- SECURITY ----------------
SECRET_KEY = 'django-insecure-9=r*$tie0z8gmlwygy*5hx5_qe=c8c1j6h*6f+(7+xd&+c&1p+'

DEBUG = False

ALLOWED_HOSTS = ['*']


# ---------------- APPLICATIONS ----------------
INSTALLED_APPS = [
    'ibasco_league_app.apps.IbascoLeagueAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# ---------------- MIDDLEWARE ----------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # IMPORTANT
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'ibasco_league.urls'


# ---------------- TEMPLATES ----------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # keep as is
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'ibasco_league.wsgi.application'


# ---------------- DATABASE (Render Ready) ----------------
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3'
    )
}


# ---------------- PASSWORD VALIDATION ----------------
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


# ---------------- INTERNATIONAL ----------------
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Kampala'

USE_I18N = True
USE_TZ = True


# ---------------- STATIC FILES ----------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# ---------------- MEDIA FILES ----------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ---------------- WHITENOISE ----------------
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ---------------- DEFAULT FIELD ----------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'