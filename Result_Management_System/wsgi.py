"""
WSGI config for Result_Management_System project.

It exposes the WSGI callable as a course-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_course", "Result_Management_System.settings")

application = get_wsgi_application()
