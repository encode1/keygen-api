# settings/production.py

from .base import *
print('In production')

ALLOWED_HOSTS = ['*']
DEBUG = False
