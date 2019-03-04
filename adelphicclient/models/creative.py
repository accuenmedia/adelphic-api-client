import json
import requests
import datetime

from adelphicclient.models.base import Base

class Creative(Base):

    object = "creative"

    def find_by_ad_order(self, ad_order_id):
        url = "{0}/{1}/getCreativesByAdOrder/{2}".format(self.connection.url, self.object, ad_order_id)
        response = requests.get(
            url,
            auth=self.connection.authenticate(),
            verify=False
        )

        return self.get_response_list(response)