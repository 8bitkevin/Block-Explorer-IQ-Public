# -*- coding: utf-8 -*-
"""
WSGI config for fbwiki project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fbwiki.settings")
#
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()


import os
import time
import traceback
import signal
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fbwiki.settings")

try:
    application = get_wsgi_application()
    print('WSGI started')
except Exception:
    print('handling WSGI exception')
    # Error loading applications
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)


