from __future__ import absolute_import, print_function

from django.conf import settings

CONF_OBJ = getattr(settings, 'UAA_CONF', None)

CLIENT_ID = CONF_OBJ.get('clientid', None)

CLIENT_SECRET = CONF_OBJ.get('clientsecret', None)

BASE_DOMAIN = CONF_OBJ.get('url', None)

APP_NAME = CONF_OBJ.get('xsappname', None)

SCOPE = APP_NAME + ".login"

ACCESS_TOKEN_URL = '{0}/oauth/access_token'.format(BASE_DOMAIN)
AUTHORIZE_URL = '{0}/oauth/authorize'.format(BASE_DOMAIN)
