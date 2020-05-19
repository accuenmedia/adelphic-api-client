import unittest
import json

import config

from adelphicclient.models.deals import Deal
from adelphicclient.service.connection import Connection


class DealTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.connection = Connection(config.USERNAME, config.PASSWORD)

    def test_get_all_exchanges(self):
        deal_service = Deal(connection=self.connection)

        deals_string = deal_service.get_all()
        deals = json.loads(deals_string)

        self.assertEqual(deals["response_code"], 200)
        self.assertEqual(len(deals["data"]), 645) # total deals as of 5/19/20
