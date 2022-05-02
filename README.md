# Sample Flask API
    - Flask, Marshmallow, SQLAlchemy, and PostgreSQL
    - General MVC design
    - Unit testing for endpoints

# Creating databases
    1. Create testing and development PostgreSQL database
    2. Adjust SQLALCHEMY_DATABASE_URI in config/development.py and config/testing.py 

# Running development server
    1. pipenv install --dev
    2. pipenv shell
    3. export FLASK_ENV=development && flask run

# Test suite (pytest)
    1. pipenv shell python -m pytest

# General Resources:
- Flask and MVC    
    * https://python.plainenglish.io/flask-crud-application-using-mvc-architecture-3b073271274f
- Flask testing
    * https://flask.palletsprojects.com/en/2.1.x/testing/
    * https://testdriven.io/blog/flask-pytest/
- SQLAlchemy Relationships
    * https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
    * https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
- Error Handlers
    * https://flask.palletsprojects.com/en/2.1.x/errorhandling/