import json
import requests
import datetime

from adelphicclient.models.base import Base

class Exchange(Base):

    object = "exchange"

    def get_all(self):
        url = f"{self.connection.url}/{self.object}/getAllExchanges"
        response = self.make_request("GET", url)

        return self.get_response_list(response)
