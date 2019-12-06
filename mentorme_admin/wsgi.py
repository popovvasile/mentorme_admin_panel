"""
WSGI config for mentorme_admin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mentorme_admin.settings")
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

application = get_wsgi_application()

application = WhiteNoise(application, root=os.path.join(PROJECT_ROOT,'static/' ))