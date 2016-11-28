"""
Django settings for hello project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'p0yqa%-slv1e#@dab(-)622@1fd4=by25hn+pp(fi-(6shs6o2'


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

TEMPLATE_DEBUG = True

# ALLOWED_HOSTS = ['target.pythonanywhere.com']
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'polls',
    'quadratic',
    'courses',
    'students',
    'coaches',
    'feedbacks',

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

ROOT_URLCONF = 'pybursa.urls'

WSGI_APPLICATION = 'pybursa.wsgi.application'


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

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/bootstrap'), )

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )

# ADMINS = (
#         ('Nikolay Borovenskiy', 'nikolay.borovenskiy@gmail.com'),
#         ('Ivan Babaiev', 'ivanbabaiev@gmail.com'),
#     )
#
# EMAIL_HOST = 'mx1.mirohost.net'
#
# EMAIL_PORT = 25
#
# EMAIL_HOST_USER = 'pybursa@mdcexpert.com'
#
# EMAIL_HOST_PASSWORD = 'x9AgUkx6'
#
# SERVER_EMAIL = 'pybursa@mdcexpert.com'
#
# DEFAULT_FROM_EMAIL = 'pybursa@mdcexpert.com'
#
# EMAIL_SUBJECT_PREFIX = '[My Feedback] '
#
# EMAIL_USE_TLS = False


# EMAIL_BACKEND = "ivanbabaiev@gmail.com"
# # SENDGRID_API_KEY = "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"
# SENDGRID_API_KEY = "WNOS0Cw7QwCqOXvBggg9RQ"

# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
#
# send_mail("Your Subject", "This is a simple text email body.",
#   "Ivan Babaiev <hello@yamilasusta.com>", ["yamil@sendgrid.com"])


EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
ADMINS = (
    ('Nikolay Borovenskiy', 'nikolay.borovenskiy@gmail.com'),
    ('Ivan Babaiev', 'ivanbabaiev@gmail.com'), )

# debug
LOGGING = {
    'version': 1,
    'loggers': {
        'courses': {
            'level': 'DEBUG',
            'handlers': ['course_handler'],
        },
        'students': {
            'level': 'WARNING',
            'handlers': ['student_handler'],
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'course_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
            'formatter': 'simple',
        },
        'student_handler': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'students_logger.log'),
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
}
'''
try:
    from local_settings import *
except ImportError:
    print "Warning! local_settings are not defined!"
'''
