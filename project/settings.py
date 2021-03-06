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

ADMINS = (
    ('Support', SUPPORT_EMAIL),
)

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'logging.NullHandler'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_seo_js.middleware.escaped_fragment': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_seo_js.middleware.hashbang': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_seo_js.middleware.useragent': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
if ENV == 'production':
    LOGGING['loggers'] = {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_seo_js.middleware.escaped_fragment': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_seo_js.middleware.hashbang': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_seo_js.middleware.useragent': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
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
    'django.contrib.sites',
    'storages',
    'jsonview',
    'easy_thumbnails',
    'oauth2_provider',
    'modeltranslation',
    'favicon',
    'app.account',
    'app.file',
    'app.home',
    'app.tag',
    'app.image',
    'app.project',
    'app.post',
    'app.contact',
    'app.manager',
    'app.user_app',
    'django_seo_js'
)

MIDDLEWARE_CLASSES = (
    'django_seo_js.middleware.EscapedFragmentMiddleware',  # If you're using #!
    'django_seo_js.middleware.UserAgentMiddleware',  # If you want to detect by user agent
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'app.account.middleware.access.AccessViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'solid_i18n.middleware.SolidLocaleMiddleware'
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

# Parse database configuration from $DATABASE_URL
if os.environ.get('DATABASE_URL', None) is not None and not USE_SQLITE:
    DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'))

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en')

# supported languages
LANGUAGES = (
    ('en', 'EN'),
    ('ru', 'RU'),
)

MODELTRANSLATION_LANGUAGES = ('en', 'ru')

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'app')
]

SOLID_I18N_HANDLE_DEFAULT_PREFIX = True

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

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

THUMBNAIL_SUBDIR = 'thumbnail'

FAVICON_CONFIG = {
    'shortcut icon': [16 ,32 ,48 ,128, 192],
    'touch-icon': [196],
    'icon': [196],
    'apple-touch-icon': [57, 72, 114, 144, 180],
    'apple-touch-icon-precomposed': [57, 72, 76, 114, 120, 144, 152,180],
}

# Backend to use
SEO_JS_PRERENDER_TOKEN = os.environ.get('SEO_JS_PRERENDER_TOKEN', False)

SEO_JS_PRERENDER_CUSTOM = os.environ.get('SEO_JS_PRERENDER_CUSTOM', 0) == '1'

if SEO_JS_PRERENDER_TOKEN == '' or not SEO_JS_PRERENDER_TOKEN or SEO_JS_PRERENDER_CUSTOM:
    SEO_JS_BACKEND = "app.manager.html_cache.prerender.CustomPrerenderIO"
else:
    SEO_JS_BACKEND = "django_seo_js.backends.PrerenderIO"

SEO_JS_PRERENDER_URL = os.environ.get('SEO_JS_PRERENDER_URL', '')  # Note trailing slash.
SEO_JS_PRERENDER_RECACHE_URL = os.environ.get('SEO_JS_PRERENDER_RECACHE_URL', '')

# Whether to run the middlewares and update_cache_for_url.  Useful to set False for unit testing.
SEO_JS_ENABLED = True  # Defaults to *not* DEBUG.

if os.environ.get('SEO_JS_PRERENDER_TIMEOUT', False):
    SEO_JS_PRERENDER_TIMEOUT = float(os.environ.get('SEO_JS_PRERENDER_TIMEOUT', False))
else:
    SEO_JS_PRERENDER_TIMEOUT = False

SEO_JS_USER_AGENTS = [
    'Facebot',
    "Twitterbot"
]
