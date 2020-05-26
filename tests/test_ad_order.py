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

        ad_orders_string = ad_order_service.find_by_campaign(198127)
        ad_orders = json.loads(ad_orders_string)

        self.assertEqual(ad_orders["response_code"], 200)
        self.assertEqual(len(ad_orders["data"]), 1)

    def test_get_by_id(self):
        ad_order_service = AdOrder(connection=self.connection)

        url = "getAdOrder?id=1220142"

        ad_order_string = ad_order_service.get_by_id(url)
        ad_order = json.loads(ad_order_string)

        self.assertEqual(ad_order["response_code"], 200)
        self.assertEqual(ad_order["data"]["name"], "JH Test Ad Order")
