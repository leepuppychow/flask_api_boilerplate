from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from errors.handlers import register_error_handlers

db = SQLAlchemy()

# Import blueprints:
from routes.dog_blueprint import dog_blueprint as dog_blueprint_v1
from routes.toy_blueprint import toy_blueprint as toy_blueprint_v1
from routes.park_blueprint import park_blueprint as park_blueprint_v1

def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()

    # Register routes here:
    app.register_blueprint(dog_blueprint_v1, url_prefix='/api/v1/dogs')
    app.register_blueprint(toy_blueprint_v1, url_prefix='/api/v1/dogs/<int:dog_id>/toys')
    app.register_blueprint(park_blueprint_v1, url_prefix='/api/v1/dogs/<int:dog_id>/parks')

    # Register error handlers after blueprints:
    register_error_handlers(app)
    return app

app = create_app('config.development')

if __name__ == '__main__':
    app.run(debug=True)