"""
ASGI config for mm_authservice project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
import logging

logger = logging.getLogger('authservice')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mm_authservice.settings")

logger.info('Starting ASGI application for mm_authservice...')
application = get_asgi_application()
logger.info('ASGI application for mm_authservice is ready.')