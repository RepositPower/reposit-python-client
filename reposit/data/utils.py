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
