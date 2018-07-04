from reposit.auth.connect import RPConnection
from reposit.data.utils import api_response


class RepositController(object):

    def __init__(self, auth):
        self.auth_headers = {
            'Authorization': 'Bearer {}'.format(auth.token),
            'Reposit-Auth': 'API'
        }
        self.user_key = self._get_user_key()

    def _get_user_key(self):
        """
        Retrieve the user key used for subsequent requests
        :param auth_headers:
        :return:
        """
        return api_response(
            url='https://{}/v2/userkeys',
            controller=self,
            field='userKeys',
            subfield=0,
            no_user_key=True
        )

    @property
    def battery_capacity(self):

        return api_response(
            url='https://{}/v2/deployments/{}/battery/capacity',
            controller=self,
            field='batteryCapacity'
        )

    @property
    def battery_min_state_of_charge(self):

        return api_response(
            url='https://{}/v2/deployments/{}/battery/min_soc',
            controller=self,
            field='min_soc'
        )

    @property
    def has_battery(self):

        return api_response(
            url='https://{}/v2/deployments/{}/components',
            controller=self,
            field='data',
            subfield='battery',
        )

    @property
    def has_inverter(self):

        return api_response(
            url='https://{}/v2/deployments/{}/components',
            controller=self,
            field='data',
            subfield='inverter',
        )

    @property
    def historical_generation(self):
        """
        Return a list of data points as lists. Time are in GMT
        :return:
        """

        return api_response(
            url='https://{}/v2/deployments/{}/generation/historical/p',
            controller=self,
            field='solarP',
            format_list=True
        )

    @property
    def historical_grid_credits(self):
        pass


user = RPConnection('zeo@zeo.com', 'Reposit1')
rp = RepositController(user)


print(rp.historical_generation)