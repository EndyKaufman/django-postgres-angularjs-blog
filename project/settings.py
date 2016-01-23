"""
Django settings for work1 project, on Heroku. Fore more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import dj_database_url

# SITE CONFIG
SITE_NAME = u'django-postgres-angularjs-blog'
SITE_HASH_TAG = u'#myblog'
SHORT_SITE_NAME = u'My Blog'
ON_PRODUCTION = os.environ.get('ON_PRODUCTION', None) == '1'
USE_AMAZONE = os.environ.get('USE_AMAZONE', None) == '1'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i+acxn5(akgsn!sr4^qgf(^m&*@+g1@u^t@=8s@axc41ml*f=s'

# SECURITY WARNING: don't run with debug turned on in production!
if ON_PRODUCTION:
    DEBUG = False
    TEMPLATE_DEBUG_MODE = False
else:
    DEBUG = True
    TEMPLATE_DEBUG_MODE = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'livereload',
    'django.contrib.staticfiles',
    'storages',
    'jsonview',
    'app.myauth',
    'app.home',
    'app.project'
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '%s/app' % BASE_DIR
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'debug': TEMPLATE_DEBUG_MODE,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST_NAME': os.path.join(BASE_DIR, 'test.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True

# Parse database configuration from $DATABASE_URL
if os.environ.get('DATABASE_URL', None) != None:
    DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'))

# DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_LOCATION = 'static'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/%s/' % STATICFILES_LOCATION

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
if not USE_AMAZONE:
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
else:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
    AWS_PRELOAD_METADATA = True  # necessary to fix manage.py collectstatic command to only upload changed files instead of all files

    STATIC_URL = 'http://%s.s3.amazonaws.com/%s/' % (AWS_STORAGE_BUCKET_NAME, STATICFILES_LOCATION)
