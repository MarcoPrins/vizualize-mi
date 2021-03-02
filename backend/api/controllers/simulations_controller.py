from services.simulator import Simulator
from helpers.database import execute_sql
from flask_restful import Resource, reqparse


class SimulationsController(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('number_of_requests', type=int, required=True)
        parser.add_argument('region_id', type=str, required=True)
        args = parser.parse_args()

        regions = execute_sql(
          """
            select min_longitude, min_latitude, max_longitude, max_latitude
            from region_bounding_box
            where region_id = ?
          """,
          [args['region_id']]
        )

        if (len(regions) > 0):
            result = Simulator(regions[0]).simulate(args['number_of_requests'])
            return result, 200
        else:
            return {"message": "Region not found"}, 404
