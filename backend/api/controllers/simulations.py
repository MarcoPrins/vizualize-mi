from services.simulator import Simulator
from flask_restful import Resource, reqparse
from helpers.database import execute_sql

parser = reqparse.RequestParser()
parser.add_argument('number_of_requests', type=int)
parser.add_argument('region_id', type=str)

class Simulations(Resource):
    def post(self):
        args = parser.parse_args()
        region = execute_sql(
          """
            select min_longitude, min_latitude, max_longitude, max_latitude
            from region_bounding_box
            where region_id = ?
          """,
          [args['region_id']]
        )[0]
        result = Simulator(region).simulate(args['number_of_requests'])
        return {"status": "success", "message": result}
