import requests
import json
from random import randint
from unittest import TestCase, main

LIVE_URL = 'https://settings.microapi.dev/v1/'
LOCAL_HOST_URL = 'http://127.0.0.1:5000/v1/'
BASE_URL = LOCAL_HOST_URL
TEST_INSTANCE_NUMBER = randint(0, 20000)
