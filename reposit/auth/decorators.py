"""
Decorators relevant to authentication
"""
from functools import wraps

import arrow

from reposit.auth.exceptions import NoAuthenticationError


def requires_auth(obj):
    """
    Check that a token exists, and request another one if it has expired.
    :return:
    """

    def decorator(func):
        @wraps(func)
        def decorated_func(*args, **kwargs):
            obj = args[0]

            if not obj.token:
                raise NoAuthenticationError

            # check if the token is still valid
            if obj.token_expiry - arrow.now().timestamp < 0:
                obj._login()

            return func(*args, **kwargs)
        return decorated_func
    return decorator
