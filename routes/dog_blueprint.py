from flask import Blueprint

from controllers.dog_controller import DogController

dog_blueprint = Blueprint('dog_blueprint', __name__)

dog_blueprint.route('', methods=['GET'])(DogController.index)
dog_blueprint.route('/', methods=['GET'])(DogController.index)
dog_blueprint.route('/', methods=['POST'])(DogController.create)
dog_blueprint.route('/<int:dog_id>', methods=['GET'])(DogController.show)
dog_blueprint.route('/<int:dog_id>', methods=['PUT'])(DogController.update)
dog_blueprint.route('/<int:dog_id>', methods=['DELETE'])(DogController.delete)
