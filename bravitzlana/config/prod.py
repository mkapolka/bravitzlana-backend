from bravitzlana.config.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bravitzlana',
        'USER': 'bravitzlana',
        'PASSWORD': os.environ['PSQL_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': 5432
    }
}

DEBUG = False

ALLOWED_HOSTS = ['.bravitzlana.com', 'bravitzlana.com']
