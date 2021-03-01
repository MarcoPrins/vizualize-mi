from . import api
from api.controllers.simulations import Simulations

api.add_resource(Simulations, "/simulations")
