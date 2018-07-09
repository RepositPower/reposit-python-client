"""
Utility functions for Reposit Client
"""
import six


def dict_iter(_dict):
    """
    Python 3 / Python2 items in a dict
    :param _dict: regular ol' dict
    :return: Representation of the keys/values in a dict in either a 3
    or 2 way.
    """
    return _dict.items() if six.PY3 else _dict.iteritems()
