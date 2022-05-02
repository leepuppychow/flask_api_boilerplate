from flask import Blueprint

from controllers.sample_controller import SampleController

sample_blueprint = Blueprint('sample_blueprint', __name__)


sample_blueprint.route('', methods=['GET'])(SampleController.index)