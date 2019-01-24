"""
Exceptions relating to auth
"""


class NoAuthenticationError(Exception):
    """
    If a method is called that requires an access token and none is yet
    set then raise this error
    """
    # pylint: disable=unnecessary-pass
    pass
