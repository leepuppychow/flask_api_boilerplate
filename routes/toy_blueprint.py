from flask import Blueprint

from controllers.toy_controller import ToyController

toy_blueprint = Blueprint('toy_blueprint', __name__)

toy_blueprint.route('', methods=['GET'])(ToyController.index)
toy_blueprint.route('/', methods=['GET'])(ToyController.index)
toy_blueprint.route('', methods=['POST'])(ToyController.create)
toy_blueprint.route('/', methods=['POST'])(ToyController.create)
