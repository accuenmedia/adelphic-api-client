import json
import requests
import datetime

from adelphicclient.models.base import Base

class Audience(Base):

    object = "audience"

    # TODO: need get/set sitelist, set deals, set exchanges
    # TODO: adelphic to confirm exchange availability

    def __init__(self, connection=None):
        super().__init__(connection)

        self.domains = []
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

    # def update(self, audience_id):
    #     url = "{0}/{1}/getAdOrdersByCampaign?id={2}".format(self.connection.url, self.object, id)
    #     response = self.make_request("GET", url)

    #     return self.get_response_list(response)


