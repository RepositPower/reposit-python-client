"""
Define an API connection object
"""
import logging

import requests
import pendulum

from reposit.data.exceptions import InvalidControllerException
from reposit.data.utils import is_valid_url, deepest_key, match_to_schema
from reposit.settings import BASE_URL

logger = logging.getLogger(__name__)


class ApiRequest(object):
    """
    A class which represents a request/response from the Reposit API.

    Why a class and not a function?
    well we can do some comprehensive validation and checking on creation
    """
    def __str__(self):
        """
        This should give us a good idea (for debugging)
        exactly the request and what data we wanted.
        We don't want to log the controller object as this
        will leak the access token.
        :return:
        """
        return '{} {}'.format(self.url, self.schema)

    def __init__(self, path, controller, schema, **kwargs):
        """
        :param path: the url endpoint (e.g. /v2/deployments etc. etc.
        :param controller: a Controller instance
        :param schema: A dict representing the structure of the response.
        E.g. we want houseP and the API returns the following:
        {
            "data": {
                "houseP": {'blah'}
            }
        }
        So the schema in this case should be a dict like so:
        {
            "data": {
                "houseP": {}
            }
        }
        This is because some of the API responses vary in structure, so
        we can define them on the fly easily :)

        :param kwargs: additional arguments when requesting data
        """
        if path.startswith('/'):
            self.url = '{}{}'.format(BASE_URL, path)
        else:
            self.url = '{}/{}'.format(BASE_URL, path)

        assert is_valid_url(self.url)

        if not controller.auth_headers:
            raise InvalidControllerException
        self.controller = controller

        # a lookup of the response schema
        self.schema = schema

    def get(self):
        """
        Once a connection is defined as valid, then a request can be
        made. This formats the response as well as checks the response
        returns an OK http code
        :return:
        """
        resp = requests.get(
            self.url,
            headers=self.controller.auth_headers
        )
        try:
            resp.raise_for_status()
        except Exception as ex:
            # Hijack the exception to log the exact issue.
            logger.exception('Error retrieving data: {}'.format(self))
            raise ex

        data = self._simple_format_for_fields(resp)
        return data

    def query(self, start, end=None):
        """
        Similar to get() but with specified query parameters.
        :param start: unix timestamp (start of query)
        :param end: unix timestamp (end of query). If not specified
        then this defaults to now()
        :return:
        """
        if not end:
            end = pendulum.now().int_timestamp

        resp = requests.get(
            '{}?start={}&end={}'.format(self.url, start, end),
            headers=self.controller.auth_headers
        )
        try:
            resp.raise_for_status()
        except Exception as ex:
            # Hijack the exception to log the exact issue.
            logger.exception('Error retrieving data: {}'.format(self))
            raise ex

        data = self._simple_format_for_fields(resp)
        return {'data': data[0]}  # because this is a list of lists

    def _simple_format_for_fields(self, api_response):
        """
        Based on the schema provided, format the data accordingly.

        :return:
        """

        data = api_response.json()
        target_key = deepest_key(self.schema)
        target_data = match_to_schema(data, target_key)
        return target_data
