"""
Global variables for the library
"""
import os
BASE_URL = os.environ.get('BASE_URL')
AUTH_PATH = os.environ.get('AUTH_PATH', '{}/v2/auth/login/').format(BASE_URL)
