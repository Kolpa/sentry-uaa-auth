from __future__ import absolute_import, print_function

from sentry.auth.exceptions import IdentityNotValid
from sentry.auth.providers.oauth2 import OAuth2Provider, OAuth2Login, OAuth2Callback

from six.moves.urllib.parse import parse_qsl
from sentry.http import safe_urlopen, safe_urlread
from sentry.utils import json
from sentry.utils.http import absolute_uri

from .constants import (
    AUTHORIZE_URL, ACCESS_TOKEN_URL, CLIENT_ID, CLIENT_SECRET, SCOPE
)

import logging


logger = logging.getLogger(__name__)


class FixedOAuth2Callback(OAuth2Callback):
    def exchange_token(self, request, helper, code):
        # TODO: this needs the auth yet
        data = self.get_token_params(
            code=code,
            redirect_uri=absolute_uri(helper.get_redirect_url()),
        )
        req = safe_urlopen(self.access_token_url, data=data)
        body = safe_urlread(req)

        logger.warning("Next is going to be the body: %s" % body)
        logger.warning(body)
        return body


class CFUaaProvider(OAuth2Provider):
    access_token_url = ACCESS_TOKEN_URL
    authorize_url = AUTHORIZE_URL
    name = 'UAA'
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET
    scope = SCOPE

    def get_auth_pipeline(self):
        return [
            OAuth2Login(
                authorize_url=self.authorize_url,
                client_id=self.client_id,
                scope=self.scope,
            ),
            FixedOAuth2Callback(
                access_token_url=self.access_token_url,
                client_id=self.client_id,
                client_secret=self.client_secret,
            ),
        ]

    def get_refresh_token_url(self):
        return ACCESS_TOKEN_URL

    def build_identity(self, state):
        data = state['data']
        user_data = state['user']
        return {
            'id': user_data['id'],
            'email': user_data['email'],
            'name': user_data['name'],
            'data': self.get_oauth_data(data),
        }
