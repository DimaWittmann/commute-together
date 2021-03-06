"""
Django settings for commute_together project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from django.conf import settings
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

DATETIME_FORMAT = 'd.m.Y H:i'
DATE_FORMAT = 'd.m.Y'
TIME_FORMAT = 'H:i'
DATETIME_INPUT_FORMATS = ('%d.%m.%Y %H:%M', )

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xg_v6tdn3f28qqtq1nx&y0a18*)0d#-m-j!^!x@p$0js3gnju5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

VK_APP_ID = '4971550'
VKONTAKTE_APP_ID = VK_APP_ID
VK_API_SECRET = 'YNij1ROamWaRwB06C99P'
VKONTAKTE_APP_SECRET = VK_API_SECRET

LOGIN_URL = ('http://oauth.vk.com/authorize?client_id=%s&scope=email,offline&'
    'redirect_uri=http://dimawittmann.pythonanywhere.com/meeting/vklogin&response_type=code&v=5.34') % (VK_APP_ID, )
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'commute_together',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS =(
    'commute_together.vk_backend.VkBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'commute_together.urls'

WSGI_APPLICATION = 'commute_together.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

#USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT ='/home/DimaWittmann/commute_together/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)