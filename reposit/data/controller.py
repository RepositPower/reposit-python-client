"""
Defines the class that wraps around the Reposit API
"""
from __future__ import absolute_import

from reposit.auth.decorators import requires_auth
from reposit.data.utils import api_response, device_summary


class RepositController(object):
    """
    An object representing a Reposit Box.
    """
    def __init__(self, auth):

        self.auth_headers = {
            'Authorization': 'Bearer {}'.format(auth.token),
            'Reposit-Auth': 'API'
        }
        self.user_key = self._get_user_key()
        self.connection = auth

    @requires_auth
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
    @requires_auth
    def battery_capacity(self):
        """
        Return the kwh battery capacity
        :return:
        """
        return api_response(
            url='https://{}/v2/deployments/{}/battery/capacity',
            controller=self,
            field='batteryCapacity'
        )

    @property
    @requires_auth
    def battery_min_state_of_charge(self):
        """
        Return the minimum state of charge of the battery
        :return:
        """
        return api_response(
            url='https://{}/v2/deployments/{}/battery/min_soc',
            controller=self,
            field='min_soc'
        )

    @property
    @requires_auth
    def has_battery(self):
        """
        If the system has a battery installed
        :return:
        """
        return api_response(
            url='https://{}/v2/deployments/{}/components',
            controller=self,
            field='data',
            subfield='battery',
        )

    @property
    @requires_auth
    def has_inverter(self):
        """
        If the system has an inverter installed
        :return:
        """
        return api_response(
            url='https://{}/v2/deployments/{}/components',
            controller=self,
            field='data',
            subfield='inverter',
        )

    @property
    @requires_auth
    def latest_historical_generation(self):
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
    @requires_auth
    def latest_historical_grid_credits(self):
        """
        Return a list of data points as lists. Times are in GMT
        :return:
        """
        return api_response(
            url='https://{}/v2/deployments/{}/gridcredits/historical',
            controller=self,
            field='gridcredits',
            format_list=True
        )

    @property
    @requires_auth
    def weekday_tou_tariff(self):
        """
        Returns a list of dicts of weekday time of use tariff information
        :return:
        """
        return api_response(
            url='https://{}/v2/deployments/{}/tariff/tou',
            controller=self,
            field='weekday'
        )

    @property
    @requires_auth
    def weekend_tou_tariff(self):
        """
        Returns a list of dicts of weekend time of use tariff information
        :return:
        """
        return api_response(
            url='https://{}/v2/deployments/{}/tariff/tou',
            controller=self,
            field='weekend'
        )

    @property
    @requires_auth
    def feed_in_tariff(self):
        """
        The feed in tariff cost as a float
        :return:
        """
        return api_response(
            url='https://{}/v2/deployments/{}/tariff/tou',
            controller=self,
            field='fit'
        )

    @property
    @requires_auth
    def summary(self):
        """
        Return current system information as a dict
        :return:
        """
        return device_summary(self)
