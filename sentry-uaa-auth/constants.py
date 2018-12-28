from __future__ import absolute_import, print_function

from django.conf import settings

CONF_OBJ = getattr(settings, 'UAA_CONF', None)

CLIENT_ID = getattr(CONF_OBJ, 'clientid', None)

CLIENT_SECRET = getattr(CONF_OBJ, 'clientsecret', None)

BASE_DOMAIN = getattr(CONF_OBJ, 'url', None)

APP_NAME = getattr(CONF_OBJ, 'xsappname', None)

SCOPE = APP_NAME + ".login"

ACCESS_TOKEN_URL = 'https://{0}/oauth/access_token'.format(BASE_DOMAIN)
AUTHORIZE_URL = 'https://{0}/oauth/authorize'.format(BASE_DOMAIN)
