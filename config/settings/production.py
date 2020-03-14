# settings/production.py
import dj_database_url
from .base import *
print('In production')

ALLOWED_HOSTS = ['*']
DEBUG = True
INSTALLED_APPS += ('whitenoise.runserver_nostatic',)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE += ('whitenoise.middleware.WhiteNoiseMiddleware',)

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# Enable Persistent Connections
DATABASES['default']['CONN_MAX_AGE'] = 500


#location where django collect all static files
STATIC_ROOT = os.path.join(BASE_DIR,'static')
# location where you will store your static files
STATICFILES_DIRS = [os.path.join(BASE_DIR,'project_name/static')
]