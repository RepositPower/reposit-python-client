"""
Establish a connection with the auth endpoints
"""
from __future__ import absolute_import

import logging

import requests
from requests import HTTPError

from requests.auth import HTTPBasicAuth
from reposit.settings import AUTH_PATH

logger = logging.getLogger(__name__)


class RPConnection:
    """
    Establish a connection to the Reposit cloud
    """
    def _login(self):
        """
        Given a username and password, obtain an access token
        :return:
        """
        resp = requests.post(AUTH_PATH, auth=HTTPBasicAuth(self.username, self.password), headers={
            "Reposit-Auth": "API"
        })
        try:
            resp.raise_for_status()
        except HTTPError:
            if resp.status_code in (401, 403):
                logger.exception('Unauthorized. Please check your credentials are correct.')
            logger.exception('Unable to authenticate - please try again later.')
            return None, None
        return resp.json()['access_token'], resp.json()['expires_at']

    def __init__(self, username, password):
        """
        Authenticate with a username and password.
        :param username:
        :param password:
        """
        self.username = username
        self.password = password
        self.token, self.token_expiry = self._login()

    def __str__(self):
        return self.username
