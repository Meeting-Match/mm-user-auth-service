"""
WSGI config for mm_authservice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
import logging

logger = logging.getLogger('authservice')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mm_authservice.settings")

logger.info('Starting WSGI application for mm_authservice...')
application = get_wsgi_application()
logger.info('WSGI application for mm_authservice is ready.')