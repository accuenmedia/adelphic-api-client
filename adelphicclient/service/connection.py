import requests
import json

from requests.auth import HTTPBasicAuth

class Connection:

    url_live = "https://api.adelphic.com/v1"
    url_demo = "https://api-demo2.adelphic.com/v1"

    def __init__(self, username, password, in_demo=False):
        self.username = username
        self.password = password
        if in_demo:
            self.url = self.url_demo
        else:
            self.url = self.url_live

    def authenticate(self):
        return HTTPBasicAuth(self.username, self.password)