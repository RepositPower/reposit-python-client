import requests

# from reposit.auth.connect import ENV


def get_battery_info(self):
    battery_url = 'https://{}/v2/deployments/{}/battery/capacity'.format(ENV, self.user_key)
    resp = requests.get(battery_url, headers=self.auth_headers)
    resp.raise_for_status()
    return resp.json()
