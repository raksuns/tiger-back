from .testing import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tiger',
        'USERNAME': 'postgres',
    }
}