"""
Django settings for sakuya project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=ez4-$yfy1+ad3xf%&mr0#b=*fksq91hr&m)a$%8&c!jfbvk$j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'swampdragon',
    'sakuya.accounts',
    'sakuya.photos',
    'sakuya.timeline',
    'sakuya.strength',
    'sakuya.voice',
    'sakuya.dashboard',
    'sakuya.vocaburary',
    'sakuya.motions'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'sakuya.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'sakuya/templates')],
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

WSGI_APPLICATION = 'sakuya.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (
    [
        os.path.join(BASE_DIR, 'sakuya/static'),
        os.path.join(BASE_DIR, 'sakuya/photos/static'),
        os.path.join(BASE_DIR, 'sakuya/media'),
    ]   
)

STATIC_URL = '/static/'

MEDIA_ROOT = 'sakuya/media/'

# Login redirect

LOGIN_REDIRECT_URL = '/timeline/'
LOGIN_URL = '/'

SWAMP_DRAGON_CONNECTION = ('swampdragon.connections.sockjs_connection.DjangoSubscriberConnection', '/data')

# for ec2
DRAGON_URL = 'http://52.68.38.0:9999/'
SWAMP_DRAGON_HOST = '0.0.0.0'
SWAMP_DRAGON_PORT = '9999'
SWAMP_DRAGON = { 'fff': 'sss' }

# for local
#DRAGON_URL = 'http://192.168.11.11:9999/'
#SWAMP_DRAGON_HOST = '192.168.11.11'
#SWAMP_DRAGON_PORT = '9999'
