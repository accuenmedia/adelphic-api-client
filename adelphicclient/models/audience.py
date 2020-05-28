import json
import requests
import datetime

from adelphicclient.models.base import Base

class Audience(Base):

    object = "audience"

    # TODO: need get/set sitelist, set deals, set exchanges
    # UPDATE: publishers == exchanges, per Adelphic

    def __init__(self, connection=None):
        super().__init__(connection)

        self.sitelists = []
        self.deals = []
        self.exchanges = []

    def create(self, adorder_id):
        url = f"{self.connection.url}/{self.object}/save?adorder_id={adorder_id}"

        data = {
            "name": "Test Audience",
            "target": "publisher:[\"37\"]",
            "exclude": None
        }

        response = self.make_request("POST", url, data=json.dumps(data))

        return self.get_response_list(response)

    def update(self, adorder_id, audience_id):
        url = f"{self.connection.url}/{self.object}/save?adorder_id={adorder_id}"

        data = {
            "id": audience_id,
            "name": "Test Audience", # doesn't work without setting name every time.
            "target": "publisher:[\"8\"]",
            "exclude": None
        }

        response = self.make_request("POST", url, data=json.dumps(data))

        return self.get_response_list(response)

    def targeting_as_string(self):
        pass

