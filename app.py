from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from errors.handlers import register_error_handlers

db = SQLAlchemy()

# Import models:
from models.sample_model import SampleModel

# Import blueprints:
from routes.sample_blueprint import sample_blueprint as sample_blueprint_v1


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()

    # Register routes here:
    app.register_blueprint(sample_blueprint_v1, url_prefix='/api/v1/samples')

    # Register app-level error handlers after blueprints:
    register_error_handlers(app)
    return app

app = create_app('config.development')

if __name__ == '__main__':
    app.run(debug=True)