from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dptoextension.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2996bvjmj0bn9',
        'USER': 'azqqnsvudqdrun',
        'PASSWORD': '11aab6c5e178a17d416376d501cfdde6174d8abbb3810e0e8ee3961d8537dc3d',
        'HOST': 'ec2-52-6-143-153.compute-1.amazonaws.com',
        'PORT':'5432',
        
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
