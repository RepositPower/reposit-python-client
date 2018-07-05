"""
Define the package name and do some shortcut importing so you can just go:

`from reposit import RepositController`

"""
from __future__ import absolute_import
from reposit.auth import RPConnection
from reposit.data.controller import RepositController


name = 'reposit'
