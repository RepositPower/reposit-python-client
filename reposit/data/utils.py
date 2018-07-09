"""
Utility functions for the reposit controller
"""
from __future__ import absolute_import

import re

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


def deepest_key(_dict):
    """Return the deepest key in a dict"""
    for key, value in dict_iter(_dict):
        if isinstance(value, dict) and bool(value):
            return deepest_key(_dict[key])
        return key


def match_to_schema(_dict, requested_key):
    """
    Match the schema supplied with the response to return the
    data we requested.
    :param _dict:
    :param requested_key:
    :return:
    """
    if _dict.get(requested_key) is not None:
        return _dict[requested_key]

    for valid_key in _dict:
        if valid_key == requested_key:
            if not isinstance(_dict.get(valid_key), dict):
                return _dict[valid_key]
            else:
                continue
        elif valid_key != requested_key and isinstance(_dict.get(valid_key), dict):
            return match_to_schema(_dict[valid_key], requested_key)
    return None
