import requests
import unittest
from unittest.mock import *


class RandomUser:
    def __init__(self):
        self.url = "https://randomuser.me/api"
    def get_email(self):
        return requests.get("https://randomuser.me/api/").json().get("results", {})[0].get("email")

    def get_random_user(self):
        r = requests.get(self.url)
        return r.json()['results'][0]


    def get_random_user_gender(self, gender):
        if isinstance(gender, str) and gender in ["female", "male"]:
            r = requests.get(f'{self.url}?gender={gender}')
            return r.json()['results'][0]
        raise Exception