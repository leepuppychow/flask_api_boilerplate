# Sample Flask API
    - Flask, Marshmallow, SQLAlchemy, and PostgreSQL
    - General MVC design
    - Unit testing for endpoints

# Running development server
    1. pipenv install
    2. pipenv shell
    3. export FLASK_ENV=development && flask run

# Test suite (pytest)
    1. pipenv shell python -m pytest

# Notes:
    [x] Load CSV into postgres
        COPY dogs(name,age,description) from '/Users/leechow/Desktop/temp/flask_mvc/dogs.csv' DELIMITER ',' CSV HEADER;
        
    [x] testing of endpoints
        - https://flask.palletsprojects.com/en/2.1.x/testing/
        - https://testdriven.io/blog/flask-pytest/
    
    [ ] create boilerplate Flask app with SQLAlchemy + Marshmallow
    
    [x] One-Many relationships
        - https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
    
    [x] Many-Many relationships
        - https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
    
    [x] standard error handler
        - https://flask.palletsprojects.com/en/2.1.x/errorhandling/

    [ ] Rate limiting API
        - [Flask-Limiter](https://flask-limiter.readthedocs.io/en/stable/)

# General Resources:
    * https://python.plainenglish.io/flask-crud-application-using-mvc-architecture-3b073271274f
