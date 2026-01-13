from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    'joollab.com',
    'www.joollab.com',
    '54.180.205.253',
    'localhost',
    '127.0.0.1'
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static',]
 