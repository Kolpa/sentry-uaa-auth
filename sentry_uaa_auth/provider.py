from __future__ import absolute_import, print_function

from sentry.auth.exceptions import IdentityNotValid
from sentry.auth.providers.oauth2 import OAuth2Provider

from .constants import (
    AUTHORIZE_URL, ACCESS_TOKEN_URL, CLIENT_ID, CLIENT_SECRET, SCOPE
)


class CFUaaProvider(OAuth2Provider):
    access_token_url = ACCESS_TOKEN_URL
    authorize_url = AUTHORIZE_URL
    name = 'UAA'
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET

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
