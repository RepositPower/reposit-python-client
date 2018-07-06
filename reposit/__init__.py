"""
Define the package name and do some shortcut importing so you can just go:

`from reposit import Controller`

"""
from __future__ import absolute_import
from reposit.data.controller import Controller
from reposit.auth.account import Account

name = 'reposit'
