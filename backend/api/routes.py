from . import api
from api.controllers.simulations_controller import SimulationsController

api.add_resource(SimulationsController, "/simulations")
