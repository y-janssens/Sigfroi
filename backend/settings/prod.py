from .base import *

DEBUG = False
PROXY = "https://carrieres-marbrume.herokuapp.com"

ALLOWED_HOSTS = ['*']

DATABASES = {

    'default': env.db(),
}