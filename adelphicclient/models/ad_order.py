import json
import requests
import datetime

from adelphicclient.models.base import Base

class AdOrder(Base):

    object = "adorder"

    def find_by_campaign(self, id):
        url = "{0}/{1}/getAdOrdersByCampaign?id={2}".format(self.connection.url, self.object, id)
        response = self.make_request("GET", url)

        return self.get_response_list(response)
