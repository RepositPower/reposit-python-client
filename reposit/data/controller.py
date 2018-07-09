"""
Defines the class that wraps around the Reposit API
"""
from __future__ import absolute_import

from reposit.data.api import ApiRequest


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
        request = ApiRequest(
            path='v2/deployments/{}/battery/capacity'.format(self.user_key),
            controller=self,
            schema={'batteryCapacity': {}}
        )
        return request.get()

    @property
    def battery_min_state_of_charge(self):
        """
        Return the minimum state of charge of the battery
        :return:
        """
        request = ApiRequest(
            path='v2/deployments/{}/battery/min_soc'.format(self.user_key),
            controller=self,
            schema={'min_soc': {}}
        )

        return request.get()

    @property
    def has_battery(self):
        """
        If the system has a battery installed
        :return:
        """
        request = ApiRequest(
            path='v2/deployments/{}/components'.format(self.user_key),
            controller=self,
            schema={
                'data': {
                    'battery': {}
                }
            }
        )
        return request.get()

    @property
    def has_inverter(self):
        """
        If the system has an inverter installed
        :return:
        """
        request = ApiRequest(
            path='v2/deployments/{}/components'.format(self.user_key),
            controller=self,
            schema={
                'data': {
                    'inverter': {}
                }
            }
        )
        return request.get()

    @property
    def latest_historical_generation(self):
        """
        Return a list of data points as lists. Time are in GMT
        :return:
        """
        request = ApiRequest(
            path='v2/deployments/{}/generation/historical/p'.format(self.user_key),
            controller=self,
            schema={
                'solarP': {}
            }
        )
        return request.get()

    @property
    def latest_historical_house(self):
        """
        Return a list of data points as lists. Time are in GMT
        :return:
        """
        request = ApiRequest(
            path='v2/deployments/{}/house/historical'.format(self.user_key),
            controller=self,
            schema={
                'data': {
                    'houseP': {}
                }
            }
        )
        return request.get()

    @property
    def latest_historical_grid_credits(self):
        """
        Return a list of data points as lists. Times are in GMT
        :return:
        """

        request = ApiRequest(
            path='v2/deployments/{}/gridcredits/historical'.format(self.user_key),
            controller=self,
            schema={
                'gridcredits': {}
            }
        )
        return request.get()

    @property
    def latest_historical_inverter(self):
        """
        Return a list of data points as lists. Times are in GMT
        :return:
        """
        request = ApiRequest(
            path='v2/deployments/{}/inverter/historical/p'.format(self.user_key),
            controller=self,
            schema={
                'inverterP': {}
            }
        )
        return request.get()

    @property
    def latest_historical_meter(self):
        """
        Return a list of data points as lists. Times are in GMT
        :return:
        """
        request = ApiRequest(
            path='v2/deployments/{}/meter/historical/p'.format(self.user_key),
            controller=self,
            schema={
                'meterP': {}
            }
        )
        return request.get()

    @property
    def weekday_tou_tariff(self):
        """
        Returns a list of dicts of weekday time of use tariff information
        :return:
        """
        request = ApiRequest(
            path='v2/deployments/{}/tariff/tou'.format(self.user_key),
            controller=self,
            schema={
                'weekday': {}
            }
        )
        return request.get()

    @property
    def weekend_tou_tariff(self):
        """
        Returns a list of dicts of weekend time of use tariff information
        :return:
        """
        request = ApiRequest(
            path='v2/deployments/{}/tariff/tou'.format(self.user_key),
            controller=self,
            schema={
                'weekend': {}
            }
        )
        return request.get()

    @property
    def feed_in_tariff(self):
        """
        The feed in tariff cost as a float
        :return:
        """
        request = ApiRequest(
            path='v2/deployments/{}/tariff/tou'.format(self.user_key),
            controller=self,
            schema={
                'fit': {}
            }
        )
        return request.get()
