# -*- coding: utf-8 -*-
"""
Django settings for OMserverweb project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#Global Variable
SYSTEM_NAME="分布式业务线监控平台"
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#y)+eb7$4w8fj0qzt2e*fed&qhl9!y6@=-%7b95*u!7g(og^jr'


#IDC list
IDC={'ct':'电信','cnc':'联通','cmcc':'移动'}

#system path
RRDPATH=BASE_DIR+"/rrd"
PNGPATH=BASE_DIR+"/static/rrdtool"
MAINAPPPATH=BASE_DIR+"/webmonitor"

#rrdtool Alarm value
TIME_ALARM=1

#rrdtool time Y MAX value
TIME_YMAX=1

#rrdtool down_speed Y MAX
DOWN_APEED_YMAX=8388608

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []

INTERNAL_IPS = ('127.0.0.1','192.168.50.102',)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'webservermonitor',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'kylin',                  # Not used with sqlite3.
        'HOST': '1.1.1.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'publicclass',
    'webmonitor',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'monitor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'monitor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


#debug_toolbar
DEBUG_TOOLBAR_PANELS = (
'debug_toolbar.panels.version.VersionDebugPanel',
'debug_toolbar.panels.timer.TimerDebugPanel',
'debug_toolbar.panels.settings.SettingsPanel',
'debug_toolbar.panels.headers.HeaderDebugPanel',
'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
'debug_toolbar.panels.template.TemplateDebugPanel',
'debug_toolbar.panels.sql.SQLDebugPanel',
'debug_toolbar.panels.signals.SignalDebugPanel',
'debug_toolbar.panels.logging.LoggingPanel',
)




# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),

)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),)

LOGGING = {
     'version': 1,
     'disable_existing_loggers': True,
     'formatters': {
         'simple': {
             'format': '[%(asctime)s] %(levelname)s : %(message)s'
         },
         'verbose': {
             'format': '[%(asctime)s] %(levelname)s %(module)s %(process)d %(thread)d : %(message)s'
         },
     },
     'handlers': {
         'null': {
             'level': 'DEBUG',
             'class': 'logging.NullHandler',
         },
         'console': {
             'level': 'INFO',
             'class': 'logging.StreamHandler',
             'formatter': 'simple',
         },
         'file': {
             'level': 'INFO',
             'class': 'logging.FileHandler',
             'formatter': 'simple',
             'filename': BASE_DIR+'/sys.log',
             'mode': 'a',
         },
     },
     'loggers': {
         'django': {
             'handlers': ['file', 'console'],
             'level':'INFO',
             'propagate': True,
         },
     },
 }