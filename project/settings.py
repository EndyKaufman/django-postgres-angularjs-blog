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
ENV = os.environ.get('ENV', 'development')
USE_SQLITE = os.environ.get('USE_SQLITE', None) == '1'
USE_AMAZONE = os.environ.get('USE_AMAZONE', None) == '1'

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', '1') == '1'
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
SERVER_EMAIL = os.environ.get('EMAIL_HOST_USER', '')
SUPPORT_EMAIL = os.environ.get('SUPPORT_EMAIL', '')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Theme support
THEME = os.environ.get('THEME', 'default')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i+acxn5(akgsn!sr4^qgf(^m&*@+g1@u^t@=8s@axc41ml*f=s'

SUPPORT_EMAIL = os.environ.get('SUPPORT_EMAIL', '')
# SESSION_COOKIE_SECURE = True

# SECURITY WARNING: don't run with debug turned on in production!
if ENV == 'production':
    DEBUG = False
    TEMPLATE_DEBUG_MODE = False
else:
    DEBUG = True
    TEMPLATE_DEBUG_MODE = True

# LOGGING
if ENV == 'production':
    ADMINS = (
        ('Support', SUPPORT_EMAIL),
    )
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

# CACHE
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'jsonview',
    'django_seo_js',
    'app.account',
    'app.file',
    'app.home',
    'app.tag',
    'app.image',
    'app.project',
    'app.post',
    'app.contact',
    'app.manager'
)

MIDDLEWARE_CLASSES = (
    'django_seo_js.middleware.EscapedFragmentMiddleware',  # If you're using #!
    'django_seo_js.middleware.UserAgentMiddleware',  # If you want to detect by user agent
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
AUTH_USER_MODEL = 'account.User'

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
                'django.core.context_processors.media',
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
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
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
if os.environ.get('DATABASE_URL', None) != None and not USE_SQLITE:
    DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'))

# DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_LOCATION = 'static'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/%s/' % STATICFILES_LOCATION

MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, STATICFILES_LOCATION),
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

# Backend to use
SEO_JS_PRERENDER_TOKEN = os.environ.get('SEO_JS_PRERENDER_TOKEN', False)

if SEO_JS_PRERENDER_TOKEN == '' or not SEO_JS_PRERENDER_TOKEN:
    SEO_JS_BACKEND = "django_seo_js.backends.PrerenderHosted"
else:
    SEO_JS_BACKEND = "django_seo_js.backends.PrerenderIO"

SEO_JS_PRERENDER_URL = os.environ.get('SEO_JS_PRERENDER_URL', '')  # Note trailing slash.
SEO_JS_PRERENDER_RECACHE_URL = os.environ.get('SEO_JS_PRERENDER_RECACHE_URL', '')

# Whether to run the middlewares and update_cache_for_url.  Useful to set False for unit testing.
SEO_JS_ENABLED = True  # Defaults to *not* DEBUG.

SEO_JS_PRERENDER_TIMEOUT = float(os.environ.get('SEO_JS_PRERENDER_TIMEOUT', False))

SEO_JS_USER_AGENTS = [
    'Facebot',
    "Twitterbot"
]
