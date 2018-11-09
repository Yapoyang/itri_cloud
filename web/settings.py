"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ejqe&&b5x5#)x&=a**vup52p62)ffmf=$gdxjcs+^2#h%hu*9g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['52.198.25.52']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloud',
    'restaurants',
    'data',
    'user_output',
    'personal',
    'post',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web.urls'
SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'
LOGIN_REDIRECT_URL="/index/"
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'),],
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

WSGI_APPLICATION = 'web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'itri_db_01',
        'USER':'yapo',
        'PASSWORD':'itrieosl',
        'HOST':'52.198.25.52',
        'PORT':'3306',
        'OPTIONS':{'autocommit':True,},
    },
    'itri_db_01':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'itri_db_01',
        'USER':'yapo',
        'PASSWORD':'itrieosl',
        'HOST':'52.198.25.52',
        'PORT':'3306',
        'OPTIONS':{'autocommit':True,},
    },
    'D017C2BABA3F':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'D017C2BABA3F',
        'USER':'yapo',
        'PASSWORD':'itrieosl',
        'HOST':'52.198.25.52',
        'PORT':'3306',
        'OPTIONS':{'autocommit':True,},
    },
    'D017C2BABA63':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'D017C2BABA63',
        'USER':'yapo',
        'PASSWORD':'itrieosl',
        'HOST':'52.198.25.52',
        'PORT':'3306',
        'OPTIONS':{'autocommit':True,},
    },
    'D017C2BABDFB':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'D017C2BABDFB',
        'USER':'yapo',
        'PASSWORD':'itrieosl',
        'HOST':'52.198.25.52',
        'PORT':'3306',
        'OPTIONS':{'autocommit':True,},
    },
    'D017C2BADB63':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'D017C2BADB63',
        'USER':'yapo',
        'PASSWORD':'itrieosl',
        'HOST':'52.198.25.52',
        'PORT':'3306',
        'OPTIONS':{'autocommit':True,},
    },
    'D017C2BADB75':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'D017C2BADB75',
        'USER':'yapo',
        'PASSWORD':'itrieosl',
        'HOST':'52.198.25.52',
        'PORT':'3306',
        'OPTIONS':{'autocommit':True,},
    },
    'D017C2BAB9AD':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'D017C2BAB9AD',
        'USER':'yapo',
        'PASSWORD':'itrieosl',
        'HOST':'52.198.25.52',
        'PORT':'3306',
        'OPTIONS':{'autocommit':True,},
    },
    'D017C2BADF23':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'D017C2BADF23',
        'USER':'yapo',
        'PASSWORD':'itrieosl',
        'HOST':'52.198.25.52',
        'PORT':'3306',
        'OPTIONS':{'autocommit':True,},
    },
    'CC9F7ADAA539':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'D017C2BADF23',
        'USER':'yapo',
        'PASSWORD':'itrieosl',
        'HOST':'52.198.25.52',
        'PORT':'3306',
        'OPTIONS':{'autocommit':True,},
    },



}
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')
