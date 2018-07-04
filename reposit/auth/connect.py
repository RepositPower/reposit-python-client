import os
import logging

import requests
from requests import HTTPError
from requests.auth import HTTPBasicAuth

AUTH_URL = os.environ.get('AUTH_URL')
from reposit.data import battery
from reposit.data.utils import add_functions_as_methods

ENV = os.environ.get('ENV', 'dapi.repositpower.com')

logger = logging.getLogger(__name__)


class RPConnection(object):
    """
    Establish a connection to the Reposit cloud
    """
    def _obtain_token(self):
        """
        Given a username and password, obtain an access token
        :return:
        """
        resp = requests.post(AUTH_URL, auth=HTTPBasicAuth(self.username, self.password))
        try:
            resp.raise_for_status()
        except HTTPError:
            if resp.status_code in (401, 403):
                logger.exception('Unauthorized. Please check your credentials are correct.')
                return None
            else:
                logger.exception('Unable to authenticate - please try again later.')
                return None
        return resp.json()['access_token']

    def get_user_key(self):
        headers = {
            'Authorization': 'Bearer {}'.format(self.token),
            'Reposit-Auth': 'API'
        }
        resp = requests.get('https://{}/v2/userkeys'.format(ENV), headers=headers)
        resp.raise_for_status()
        return resp.json()['userKeys'][0]

    def __init__(self, username, password):
        """
        Authenticate with a username and password.
        :param username:
        :param password:
        """
        self.username = username
        self.password = password
        self.token = self._obtain_token()


@add_functions_as_methods([
    battery.get_battery_info
])
class Reposit(object):

    def __init__(self, auth):
        self.auth_headers = {
            'Authorization': 'Bearer {}'.format(auth.token),
            'Reposit-Auth': 'API'
        }
        self.user_key = auth.get_user_key()
