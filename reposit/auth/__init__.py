"""
Shortcut imports + checks for python versions.
"""
from __future__ import absolute_import
import sys
import logging

logger = logging.getLogger(__name__)

from reposit.auth.connect import RPConnection

if sys.version_info < (2, 5):
    raise Exception('Versions of Python older than 2.5 are not supported.')

if sys.version_info[0] != 3:
    logger.warning(
        'Python 2 is still supported, but it is recommended you adopt Python 3.'
    )
