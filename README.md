## reposit-python-client

[![Build Status](https://travis-ci.org/RepositPower/reposit-python-client.svg?branch=master)](https://travis-ci.org/RepositPower/reposit-python-client)


<p align="center">
    <span>Python client library to communicate with a Reposit Controller.</span>
</p>
<p align="center">
    <img src="https://repositpower.com/wp-content/uploads/2017/05/Reposit_13.jpg">
</p>

## Compatibility

- Python 2.7
- Python 3+ *preferred*

## Installation
```
pip install reposit
```

## Quickstart

```
from reposit.auth import RPConnection
from reposit import Controller, Account

user = RPConnection('username', 'password')
account = Account(user)

user_keys = account.get_user_keys()

controller = Controller(user, user_key=user_keys[0])

print(controller.battery_capacity)
```

## Data
| Method        | Params          | Description | Unit |
|:-------------:|:-------------|:-------------|---------|
| `battery_capacity`      | - | Get the capacity of the battery                | kWh |
| `battery_min_state_of_charge`      | -      | Get the minimum state of charge of the battery | Percentage (%)
| `has_battery` | -      | Bool of whether the user has a battery or not| True/False |
| `has_inverter` | -      | Bool of whether the user has an inverter or not| True/False |
| `get_solar_generation_data` | <ul><li>start (timestamp)</li><li>end(timestamp)(optional, default=now)</li></ul>  | Get a list of solar generation data based on start or end| kW |
|`latest_solar_generation_data`|-|Get a list of the latest generation data. Goes back the last 24 hours.| kW |
| `get_house_data` | <ul><li>start (timestamp)</li><li>end(timestamp)(optional, default=now)</li></ul>  | Get a list of house data based on start or end| kW|
|`latest_house_data`|-|Get a list of the latest house data. Goes back the last 24 hours.| kW|
| `get_battery_data` | <ul><li>start (timestamp)</li><li>end(timestamp)(optional, default=now)</li></ul>  | Get a list of battery data based on start or end| kWh |
|`latest_battery_data`|-|Get a list of the latest battery data. Goes back the last 24 hours.| kWh |pip 
| `get_meter_data` | <ul><li>start (timestamp)</li><li>end(timestamp)(optional, default=now)</li></ul>  | Get a list of meter data based on start or end. There should be at least a 5 minute gap between start and end timestamps (i.e. 300 seconds) | kWh
|`latest_meter_data`|-|Get a list of the latest meter data. Goes back the last 24 hours.| kWh |
|`feed_in_tariff`|-|Get the feed-in-tariff| Dollars ($) |

## Links

[Reposit Power](https://www.repositpower.com)
