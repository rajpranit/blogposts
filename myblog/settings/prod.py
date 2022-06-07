from .base import *

SECRET_KEY = 'django-insecure-uni%#e+87cz0cuf+z5*eb!@k$zfu-*m0f*t2ca^y_*wgn@f(p8'


DEBUG = False

ALLOWED_HOSTS = [
    'themanhwas.herokuapp.com',
]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'weebs.apps.WeebsConfig',
]
