"""
Utility functions for the reposit controller
"""
from __future__ import absolute_import

import re

import arrow
import requests
import six

from reposit.settings import BASE_URL


# adapted from Django :)
VALID_URL_REGEX = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
)


def is_valid_url(url):
    """
    Check if a url is valid for an api request.
    :param url:
    :return:
    """
    return bool(re.match(VALID_URL_REGEX, url))


def api_response(url, controller, field, subfield=None, format_list=False, no_user_key=False):
    """
    Simple data fetch for a reposit controller
    :param url: api url
    :param controller: Controller instance
    :param field: the first level field
    :param subfield: optional second level field
    :return:
    """
    subfield_check = bool(subfield)
    if subfield == 0:  # in case some fields are actually a zero
        subfield_check = True

    if no_user_key:
        resp = requests.get(url.format(BASE_URL), headers=controller.auth_headers)
    else:
        resp = requests.get(url.format(BASE_URL, controller.user_key),
                            headers=controller.auth_headers)

    resp.raise_for_status()
    if not subfield_check and not format_list:
        return resp.json()[field]

    if format_list:
        data = resp.json()
        if subfield:
            for data_point in data[field][subfield]:
                data_point[0] = arrow.get(data_point[0]).format('HH:mm:ss DD-MM-YYYY')
            return data[field][subfield]
        else:
            for data_point in data[field]:
                data_point[0] = arrow.get(data_point[0]).format('HH:mm:ss DD-MM-YYYY')
        return data[field]

    return resp.json()[field][subfield]


def device_summary(controller):
    """
    Retrieve current summary for the device
    :param controller: Controller instance
    :return:
    """
    url = '{}/v2/deployments/{}/summary/now'.format(BASE_URL, controller.user_key)
    resp = requests.get(url, headers=controller.auth_headers)
    resp.raise_for_status()
    summary = format_summary_response(resp.json())
    return summary


def format_summary_response(data):
    """
    For a summary set, pull out the interesting values
    :param data: dict of info
    :return:
    """
    response = {}
    data_items = data['data'].items() if six.PY3 else data['data'].iteritems()
    for key, value in data_items:
        if key in ('battery', 'grid', 'house', 'solar'):
            response[key] = {'state': value['state'], 'value': value['val']}
    return response
