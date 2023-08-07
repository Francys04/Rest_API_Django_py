"""
ASGI config for cados_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
"""Imports the os module, which provides functions for interacting
with the operating system, such as setting environment variables."""
import os
"""This function returns the ASGI application instance for your Django project."""
from django.core.asgi import get_asgi_application
"""This line ensures that Django knows which settings to use."""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cados_api.settings')
"""The application variable holds this ASGI application instance."""
application = get_asgi_application()
