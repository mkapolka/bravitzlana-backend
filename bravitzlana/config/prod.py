from keys import *

from bravitzlana.config.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bravitzlana',
        'USER': 'postgres',
    }
}

DEBUG = False

ALLOWED_HOSTS = ['.bravitzlana.com', 'bravitzlana.com']
