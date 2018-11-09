"""
WSGI config for web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/usr/local/lib/python3.5/dict-packages')
sys.path.append('/home/ubuntu/web')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
