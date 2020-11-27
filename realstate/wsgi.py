"""
WSGI config for realstate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

# (ADD **)
import os

from django.core.wsgi import get_wsgi_application

# (To set Django Setting modules with your app, to handle you app modules (ADD) **)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realstate.settings')

application = get_wsgi_application()
