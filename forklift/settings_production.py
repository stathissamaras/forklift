from .settings import *

# Production-specific settings
DEBUG = False
ALLOWED_HOSTS = ['cesab.gr', 'www.jasp.gr']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'forkapp',
    'bootstrap5',
    'widget_tweaks',
]

# Database settings for production (same as in settings.py)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'forkbase',
        'USER': 'postgres',
        'PASSWORD': '8365',
        'HOST': 'localhost',
    }
}

# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Email settings for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # ή τη διεύθυνση SMTP server που παρέχει ο πάροχος email
EMAIL_PORT = 587  # ή το SMTP port που παρέχει ο πάροχος email (π.χ. 465 για SSL)
EMAIL_USE_TLS = True  # Set to False if your SMTP server does not use TLS
EMAIL_HOST_USER = 'japanautospareparts@gmail.com'  # ή το όνομα χρήστη του πάροχου email
EMAIL_HOST_PASSWORD = 'kn6-cv5-kt6-g-Venok99g$'  # ή ο κωδικός πρόσβασης του πάροχου email


# Static files (CSS, JavaScript, Images)
# ... (Υπόλοιπες ρυθμίσεις που δεν αλλάζουν στην παραγωγή)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Ρυθμίσεις για το logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

django_heroku.settings(locals())
