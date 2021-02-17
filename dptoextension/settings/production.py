from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['https://extensioncyt.herokuapp.com/']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbbfssagm8arnv',
        'USER': 'ebjqgroqjepucl',
        'PASSWORD': '75058fd0bbef2dfcd73adb4afb2012256a914d324655619cb50176bfb88320d6',
        'HOST': 'ec2-52-4-171-132.compute-1.amazonaws.com',
        'PORT':'5432',
        
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)