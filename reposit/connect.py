import os
import logging

import requests
from requests import HTTPError
from requests.auth import HTTPBasicAuth

AUTH_URL = os.environ.get('AUTH_URL')


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

    def __init__(self, username, password):
        """
        Authenticate with a username and password.
        :param username:
        :param password:
        """
        self.username = username
        self.password = password
        self.token = self._obtain_token()
