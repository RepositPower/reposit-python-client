# reposit

[![Build Status](https://travis-ci.org/tombasche/reposit.svg?branch=master)](https://travis-ci.org/tombasche/reposit)


Python client library to communicate with a Reposit Controller

![](http://www.tech23.com.au/2016/wp-content/uploads/2016/09/tech23-2016-Reposit-Power-logo.png)

## Compatibility

- Python 2.7
- Python 3+
- Python 3.6 *preferred*


##Quickstart
```
from reposit.auth import RPConnection
from reposit import RepositController

user = RPConnection('username', 'password')

controller = RepositController(user)

print(controller.battery_capacity) 
```
