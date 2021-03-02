import json
import unittest
from flask import Flask, current_app

from api.tests.base import BaseTestCase
from helpers.database import execute_sql


class TestSimulations(BaseTestCase):
    """ Tests for the /simulations POST endpoint"""
    def test_simulations_success(self):
        """ POST /simulations creates a bounding box and returns the correct data """

        execute_sql(
          """
            insert into region_bounding_box(
                region_id,
                region_name,
                min_latitude,
                min_longitude,
                max_latitude,
                max_longitude
            )
            values (
                'de_berlin',
                'Berlin',
                52.527919,
                13.340148,
                52.562995,
                13.506317
            );
          """
        )

        response = self.client.post("/simulations?region_id=de_berlin&number_of_requests=2")

        # Check database
        booking_distances = execute_sql("select * from booking_distance")
        self.assertEqual(booking_distances, [])

        # Check response
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())

        self.assertEqual(
            data["booking_distance_bins"],
            {
                "From 0->1km": 0,
                "From 1->2km": 0,
                "From 2->3km": 1,
                "From 3->4km": 1
            }
        )

        self.assertEqual(type(data["most_popular_dropoff_points"]), str)
        self.assertEqual(type(data["most_popular_pickup_points"]), str)

    def test_simulations_no_region(self):
        """ POST /simulations returns 404 if there is no bounding box with specified region_id """
        response = self.client.post("/simulations?region_id=de_berlin&number_of_requests=2")

        # Check database
        booking_distances = execute_sql("select * from booking_distance")
        self.assertEqual(booking_distances, [])

        # Check response
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data.decode())

        self.assertEqual(data, {"message": "Region not found"})


if __name__ == "__main__":
    unittest.main()
