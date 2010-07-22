import os


BASE_PATH = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

INSTALLED_APPS = [
    'base',

    'templatehooks',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request',
]

TEMPLATE_DIRS = [
    os.path.join(BASE_PATH, "templates"),
]

DEBUG = True
TEMPLATE_DEBUG = DEBUG
CACHE_BACKEND = 'locmem://'
ROOT_URLCONF = 'urls'
