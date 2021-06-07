import environ
from pathlib import Path

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('users')
BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()

# Base
DEBUG = env.bool('DJANGO_DEBUG', False)

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
TIME_ZONE = 'America/Mexico_City'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# DATABASES
DATABASES = {
    #'default': env.db('DATABASE_URL'),
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# URLs
ROOT_URLCONF = 'users_api.urls'

# WSGI
WSGI_APPLICATION = 'users_api.wsgi.application'

# Apps
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'rest_framework',
    'corsheaders',
]

THIRD_PARTY_APPS = [
]
LOCAL_APPS = [
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Passwords
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]


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

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS':True,
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


# Security
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Email
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
# Admin
ADMIN_URL = 'admin/'
ADMINS = [
    ("""admin""", 'admin@admin.com'),
]
MANAGERS = ADMINS
STATIC_URL = '/static/'

dbhost="django-postgres-dep-service"
database="admin"
dbuser="sBLRWyyPsInwHftmHAWmYJURGWBGFpLs"
dbport=5432
dbpassword="tuXL3XSF8O7tsGrcGHoMos4tVNtL3tnrRshSCZokGnIfk4ArDyzaa297k2WgQPSL"