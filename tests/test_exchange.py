import unittest
import json

import config

from adelphicclient.models.exchange import Exchange
from adelphicclient.service.connection import Connection


class ExchangeTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.connection = Connection(config.USERNAME, config.PASSWORD)

    def test_get_all_exchanges(self):
        exchange_service = Exchange(connection=self.connection)

        exchanges_string = exchange_service.get_all()
        exchanges = json.loads(exchanges_string)

        self.assertEqual(exchanges["response_code"], 200)
        self.assertEqual(len(exchanges["data"]), 32)
