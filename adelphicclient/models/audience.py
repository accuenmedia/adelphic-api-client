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

        self.sitelists = ["5804"]
        self.deals = ["10172"]
        self.exchanges = ["37"]

    def create(self, adorder_id):
        url = f"{self.connection.url}/{self.object}/save?adorder_id={adorder_id}"

        targeting = self.targeting_as_string()

        data = {
            "name": "Test Audience",
            "target": targeting,
            "exclude": None
        }

        response = self.make_request("POST", url, data=json.dumps(data))

        return self.get_response_list(response)

    def update(self, adorder_id, audience_id):
        url = f"{self.connection.url}/{self.object}/save?adorder_id={adorder_id}"

        targeting = self.targeting_as_string()

        data = {
            "id": audience_id,
            "name": "Test Audience", # doesn't work without setting name every time.
            "target": targeting,
            "exclude": None
        }

        response = self.make_request("POST", url, data=json.dumps(data))

        return self.get_response_list(response)

    def targeting_as_string(self):
        exchanges = ("publisher:" + json.dumps(self.exchanges))
        deals = ("ad.pmp.deal.id:" + json.dumps(self.deals))
        sitelists = ("site.lists.v2:" + json.dumps(self.sitelists))

        string = " AND ".join((exchanges, deals, sitelists))

        return string

