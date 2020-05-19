import json
import requests
import datetime

from adelphicclient.models.base import Base

class Deal(Base):

    object = "deal"

    def get_all(self):
        url = f"{self.connection.url}/{self.object}/getAllDeals"
        response = self.make_request("GET", url)

        return self.get_response_list(response)
