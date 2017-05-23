from keys import *

from bravitzlana.config.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bravitzlana',
        'USER': 'bravitzlana',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

DEBUG = False

ALLOWED_HOSTS = ['.bravitzlana.com', 'bravitzlana.com']
