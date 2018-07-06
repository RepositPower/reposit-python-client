"""
Define an Account for a logged in user.
"""
from reposit.data.utils import api_response


class Account(object):
    """
    Represents a user account
    """
    def __init__(self, user):
        self.connection = user
        self.auth_headers = {
            'Authorization': 'Bearer {}'.format(user.token),
            'Reposit-Auth': 'API'
        }

    def get_user_keys(self):
        """
        Retrieve the user key used for subsequent requests
        :param auth_headers:
        :return:
        """
        return api_response(
            url='https://{}/v2/userkeys',
            controller=self,
            field='userKeys',
            no_user_key=True
        )
