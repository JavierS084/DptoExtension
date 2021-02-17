from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['https://dptoextension.herokuapp.com/']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dc9i7ll2vb3tgt',
        'USER': 'dpwbyxfmxspyuv',
        'PASSWORD': 'd77815aac68f5d215f55c314dbc371e0d3f6d5d315a7343145554f69b235ac27',
        'HOST': 'ec2-54-225-130-212.compute-1.amazonaws.com',
        'PORT':'5432',
        
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
