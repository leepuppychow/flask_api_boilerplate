from flask import Blueprint

from controllers.park_controller import ParkController

park_blueprint = Blueprint('park_blueprint', __name__)

park_blueprint.route('', methods=['GET'])(ParkController.index)
park_blueprint.route('/', methods=['GET'])(ParkController.index)
park_blueprint.route('', methods=['POST'])(ParkController.create)
park_blueprint.route('/', methods=['POST'])(ParkController.create)
