from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Xavfsizlik uchun o'zlashtirilgan kalit yarating
SECRET_KEY = 'django-insecure-testkey'  # Serverda buni o'zgartiring, masalan: secrets.token_urlsafe(50)

# DEBUG ni serverda False qiling
DEBUG = False  # Renderda har doim False

# Domeningizni qo'shing
ALLOWED_HOSTS = ['bmd-bino.uz', 'www.bmd-bino.uz', '*.onrender.com']  # Render domeni uchun

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',  # Sizning ilovangiz
    'whitenoise.runserver_nostatic',  # Statik fayllar uchun
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Whitenoise middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'info_site.urls'

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

WSGI_APPLICATION = 'info_site.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

# Statik fayllar sozlamalari
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Renderda statik fayllarni yig'ish uchun
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media fayllar sozlamalari
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Xavfsizlik sozlamalari
SECURE_SSL_REDIRECT = True  # Renderda HTTPS majburiy
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True