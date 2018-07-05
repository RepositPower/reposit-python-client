# reposit

[![Build Status](https://travis-ci.org/tombasche/reposit.svg?branch=master)](https://travis-ci.org/tombasche/reposit)


Library to communicate with a reposit controller

Basic usage:
```
from reposit.auth import RPConnection
from reposit import RepositController

user = RPConnection('username', 'password')

controller = RepositController(user)

print(controller.battery_capacity) 
```
