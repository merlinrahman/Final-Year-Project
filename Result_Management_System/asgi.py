"""
ASGI config for Result_Management_System project.

It exposes the ASGI callable as a course-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_course", "Result_Management_System.settings")

application = get_asgi_application()
