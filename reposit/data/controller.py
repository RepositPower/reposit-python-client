"""
Defines the class that wraps around the Reposit API
"""
from __future__ import absolute_import

from reposit.data.utils import api_response, device_summary


class Controller(object):
    """
    An object representing a Reposit Box.
    """
    def __init__(self, auth, user_key):

        self.auth_headers = {
            'Authorization': 'Bearer {}'.format(auth.token),
            'Reposit-Auth': 'API'
        }
        self.user_key = user_key
        self.connection = auth

    @property
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
    def latest_historical_house(self):
        """
        Return a list of data points as lists. Time are in GMT
        :return:
        """

        return api_response(
            url='https://{}/v2/deployments/{}/house/historical',
            controller=self,
            field='data',
            subfield='houseP',
            format_list=True
        )

    @property
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
    def latest_historical_inverter(self):
        """
        Return a list of data points as lists. Times are in GMT
        :return:
        """
        return api_response(
            url='https://{}/v2/deployments/{}/inverter/historical/p',
            controller=self,
            field='inverterP',
            format_list=True
        )

    @property
    def latest_historical_meter(self):
        """
        Return a list of data points as lists. Times are in GMT
        :return:
        """
        return api_response(
            url='https://{}/v2/deployments/{}/meter/historical/p',
            controller=self,
            field='meterP',
            format_list=True
        )


    @property
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
    def summary(self):
        """
        Return current system information as a dict
        :return:
        """
        return device_summary(self)
