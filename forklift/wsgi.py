"""
WSGI config for forklift project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Ενημερώστε την παράμετρο 'forklift.settings' ανάλογα με το περιβάλλον
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forklift.settings_development')

application = get_wsgi_application()

