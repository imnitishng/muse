import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

# Get 3rd party environment variables
def get_env_value(env_variable):
    try:
      	return os.environ[env_variable]
    except KeyError:
        error_msg = f'Set the {env_variable} environment variable'
        raise ImproperlyConfigured(error_msg)

# Spotify secrets
SPOTIFY_CLIENT_ID = get_env_value('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = get_env_value('SPOTIFY_CLIENT_SECRET')
SPOTIFY_AUTH_CODE = get_env_value('SPOTIFY_AUTH_CODE')
SPOTIFY_CLIENT_SECRET_BASE64 = get_env_value('SPOTIFY_CLIENT_SECRET_BASE64')
SPOTIFY_ACCESS_TOKEN = get_env_value('SPOTIFY_CLIENT_SECRET_BASE64')

# Database secrets
DB_HOST = os.getenv('DB_HOST', None)
DB_NAME = os.getenv('DB_NAME', None)
DB_USER = os.getenv('DB_USER', None)
DB_PASSWORD = os.getenv('DB_PASSWORD', None)

# Django Settings
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#0&uvflwtp7#lhgv6#69_!^mpaicndx@uz2b%2=b&xy$t7_4&^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
PRODUCTION = os.getenv('MUSE_PROD', True)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
FLASK_HOST = 'http://127.0.0.1:5000'
SCRAPYD_HOST = 'http://127.0.0.1:6800'

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'apps.endpoints',
    'apps.nlp',
    # rest framework
    'rest_framework' 
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'muse.urls'

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

WSGI_APPLICATION = 'muse.wsgi.application'

if PRODUCTION == False:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': '5432'
        }
    }



# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
