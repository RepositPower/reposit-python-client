"""
Define the package name and do some shortcut importing so you can just go:

`from reposit import Controller`

"""
from __future__ import absolute_import
import logging
import sys

from reposit.data.controller import Controller
from reposit.auth.account import Account

logger = logging.getLogger(__name__)

"""
Do some basic checks on the python version. We don't wan't anyone using
a deprecated version of Python, (older than 2.7). We also log a warning to
tell a consumer to use Python 3 as it would be good to stop supporting 2
completely. :)
"""
if sys.version_info < (2, 7):
    raise Exception('Versions of Python older than 2.7 are not supported.')

if sys.version_info[0] != 3:
    logger.warning(
        'Python 2 is still supported, but it is recommended you adopt Python 3.'
    )


name = 'reposit'
