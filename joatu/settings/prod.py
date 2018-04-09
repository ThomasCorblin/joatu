from joatu.settings.base import *

DEBUG = True
#ALLOWED_HOSTS = ['*']
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': os.environ.get('DATABASE_NAME', ''),
#        'USER': os.environ.get('DATABASE_USER', ''),
#        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}
#import dj_database_url
#DATABASES={
#    'default',dj_database_url.config(
#        default=os.environ.get('DATABASE_URL')
#    )
#}

#ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'joatu.middleware.LoginRequiredMiddleware',
]


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Configure Django App for Heroku.
#import django_heroku
#django_heroku.settings(locals())