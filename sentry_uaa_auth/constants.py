from __future__ import absolute_import, print_function

from cfenv import AppEnv
from django.conf import settings


cfvEnv = AppEnv()

CONF_OBJ = cfvEnv.get_service(label='xsuaa').credentials

CLIENT_ID = CONF_OBJ.get('clientid', None)

CLIENT_SECRET = CONF_OBJ.get('clientsecret', None)

BASE_DOMAIN = CONF_OBJ.get('url', None)

APP_NAME = CONF_OBJ.get('xsappname', None)

SCOPE = APP_NAME + ".login"

ACCESS_TOKEN_URL = '{0}/oauth/token'.format(BASE_DOMAIN)
AUTHORIZE_URL = '{0}/oauth/authorize'.format(BASE_DOMAIN)
