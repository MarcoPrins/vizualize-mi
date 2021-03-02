from services.simulator import Simulator
from helpers.database import execute_sql
from flask_restful import Resource, reqparse


class SimulationsController(Resource):
    def __insert_booking_distance(self, region_id, bins):
        from_0_1 = bins["From 0->1km"]
        from_1_2 = bins["From 1->2km"]
        from_2_3 = bins["From 2->3km"]
        from_3_4 = bins["From 3->4km"]

        return execute_sql(
          """
            insert into booking_distance(
                region_id,
                from_0_1,
                from_1_2,
                from_2_3,
                from_3_4
            )
            values(?,?,?,?,?)
          """,
          [region_id, from_0_1, from_1_2, from_2_3, from_3_4]
        )

    def __fetch_region(self, region_id):
        return execute_sql(
          """
            select min_longitude, min_latitude, max_longitude, max_latitude
            from region_bounding_box
            where region_id = ?
          """,
          [region_id]
        )

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("number_of_requests", type=int, required=True)
        parser.add_argument("region_id", type=str, required=True)
        args = parser.parse_args()

        regions = self.__fetch_region(args["region_id"])

        if (len(regions) > 0):
            result = Simulator(regions[0]).simulate(args["number_of_requests"])
            self.__insert_booking_distance(args["region_id"], result["booking_distance_bins"])
            return result, 200
        else:
            return {"message": "Region not found"}, 404
