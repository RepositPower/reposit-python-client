## reposit-python-client

[![Build Status](https://travis-ci.org/RepositPower/reposit-python-client.svg?branch=master)](https://travis-ci.org/RepositPower/reposit-python-client)


<p align="center">
    <span>Python client library to communicate with a Reposit Controller.</span>
</p>
<p align="center">
    <img src="http://www.tech23.com.au/2016/wp-content/uploads/2016/09/tech23-2016-Reposit-Power-logo.png">
</p>

## Compatibility

- Python 2.7
- Python 3+
- Python 3.6 *preferred*

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
| Method        | Params          | Description |
|:-------------:|:-------------|:-------------|
| `battery_capacity`      | - | Get the capacity of the battery in kWh                |
| `battery_min_state_of_charge`      | -      | Get the minimum state of charge of the battery |
| `has_battery` | -      | Bool of whether the user has a battery or not|
| `has_inverter` | -      | Bool of whether the user has an inverter or not|
| `get_historical_generation` | <ul><li>start (timestamp)</li><li>end(timestamp)(optional, default=now)</li></ul>  | Get a list of generation data based on start or end|
|`latest_historical_generation`|-|Get a list of the latest generation data. Goes back the last 24 hours.|
| `get_historical_house` | <ul><li>start (timestamp)</li><li>end(timestamp)(optional, default=now)</li></ul>  | Get a list of house data based on start or end|
|`latest_historical_house`|-|Get a list of the latest house data. Goes back the last 24 hours.|
| `get_historical_grid_credits` | <ul><li>start (timestamp)</li><li>end(timestamp)(optional, default=now)</li></ul>  | Get a list of grid credits earned based on start or end|
|`latest_historical_house`|-|Get a list of the latest grid credits earned. Goes back the last 24 hours.|
| `get_historical_inverter` | <ul><li>start (timestamp)</li><li>end(timestamp)(optional, default=now)</li></ul>  | Get a list of inverter data based on start or end|
|`latest_historical_inverter`|-|Get a list of the latest inverter data. Goes back the last 24 hours.|
| `get_historical_meter` | <ul><li>start (timestamp)</li><li>end(timestamp)(optional, default=now)</li></ul>  | Get a list of meter data based on start or end|
|`latest_historical_meter`|-|Get a list of the latest meter data. Goes back the last 24 hours.|
|`weekday_tou_tariff`|-|Get weekday tou tariff information such as peak/off peak times and rates.|
|`weekend_tou_tariff`|-|Get weekend tou tariff information such as peak/off peak times and rates.|
|`feed_in_tariff`|-|Get the feed-in-tariff|

## Links

[Reposit Power](https://www.repositpower.com)
