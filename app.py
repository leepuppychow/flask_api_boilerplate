from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import blueprints:
from routes.dog_blueprint import dog_blueprint as dog_blueprint_v1

def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()
    
    # Register routes here:
    app.register_blueprint(dog_blueprint_v1, url_prefix='/api/v1/dogs')
    return app

app = create_app('config.development')

if __name__ == '__main__':
    app.run(debug=True)