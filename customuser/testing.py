from __future__ import absolute_import, unicode_literals

from .settings import *  # noqa

MEDIA_ROOT = "/tmp"

SECRET_KEY = 'top-secret!'

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
INSTALLED_APPS += ("tests", )
