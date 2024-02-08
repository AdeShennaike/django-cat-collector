"""
Django settings for catcollector project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
# Configuration for simple JWT
from datetime import timedelta

import environ  
import dj_database_url
import django_heroku



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5xboz%bsx#farthviv^0*g9%vx0srac-epwxqh3sh!mm6f4403'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['localhost', '127.0.0.1'] # allows requests from localhost - will need to update again for deployment

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# These are required
DATABASE_URL=env('DATABASE_URL')
SECRET_KEY=env('SECRET_KEY')

# These are not required.
# If you want to connect locally to the database you may need them
# Something to be aware of, nothing more.

# PGDATABASE=env('PGDATABASE')
# PGHOST=env('PGHOST')
# PGPASSWORD=env('PGPASSWORD')
# PGPORT=env('PGPORT')
# PGUSER=env('PGUSER')


# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Adjust the port if your frontend runs on a different one
]

# Application definition

# Add 'corsheaders' to INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
  	'main_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", # Add whitenoise middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuration for django-rest-framework-simplejwt
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

ROOT_URLCONF = 'catcollector.urls'

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

WSGI_APPLICATION = 'catcollector.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': 
        dj_database_url.config('DATABASE_URL')
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'catcollector',
#         # 'HOST': 'localhost',  <-- (optional) some computers might need this line
#         # 'USER': 'cat_admin', <-- (optional) postgres user name, if you have to sign into an account to open psql, you will want to add that user name here.
#         # 'PASSWORD': 'password', <-- (optional) postgres user password, if you have to sign into an account to open psql, you will want to add that user password here.
#         # 'PORT': 3000 <-- if you desire to use a port other than 8000, you can change that here to any valid port id, some number between 1 and 65535 that isn't in use by some other process on your machine. The reason for this port number range is because of how TCP/IP works, a TCP/IP protocol network(the most widely used protocol used on the web) allocated 16 bits for port numbers. This means that number must be greater than 0 and less than 2^15 -1. 
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Add this to the very bottom of your settings.py file
# If you don't your app will not deploy properly
django_heroku.settings(locals())
