"""
Define an Account for a logged in user.
"""
from reposit.data.api import ApiRequest


class Account:
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
        request = ApiRequest(
            path='/v2/userkeys',
            controller=self,
            schema={'userKeys': {}}
        )
        return request.get()
