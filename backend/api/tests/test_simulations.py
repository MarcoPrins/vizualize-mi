import json
import unittest
from flask import Flask, current_app

from api.tests.base import BaseTestCase


class TestSimulations(BaseTestCase):
    """ Tests for the /simulations POST endpoint"""
    def test_simulations(self):
        """ Ensure the /simulations POST action behaves correctly. """
        response = self.client.post("/simulations?region_id=de_berlin&number_of_requests=2")
        # data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
