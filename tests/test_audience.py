import unittest
import json

import config

from adelphicclient.models.audience import Audience
from adelphicclient.service.connection import Connection


class AdOrderTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.connection = Connection(config.USERNAME, config.PASSWORD)

    def test_create(self):
        audience_service = Audience(connection=self.connection)

        audience_string = audience_service.create(1220142)
        audience = json.loads(audience_string)

        self.assertEqual(audience["response_code"], 200)
        self.assertEqual(len(audience["data"]), 1)

    def test_get_by_id(self):
        pass

