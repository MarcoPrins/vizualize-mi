import json
import unittest

from api.tests.base import BaseTestCase


class TestSimulationsService(BaseTestCase):
    """ Tests for the Simulation Service """

    def test_simulations(self):
        """ Ensure the /ping route behaves correctly. """
        response = self.client.get("/simulations/ping")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("pong!", data["message"])
        self.assertIn("success", data["status"])


if __name__ == "__main__":
    unittest.main()
