import unittest
import json

import config


from adelphicclient.models.ad_order import AdOrder
from adelphicclient.service.connection import Connection


class AdOrderTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.connection = Connection(config.USERNAME, config.PASSWORD)

    def test_get_ad_orders_by_campaign(self):
        ad_order_service = AdOrder(connection=self.connection)

        ad_orders_string = ad_order_service.find_by_campaign(175552)
        ad_orders = json.loads(ad_orders_string)

        self.assertEqual(ad_orders["response_code"], 200)
        self.assertEqual(len(ad_orders["data"]), 23)
