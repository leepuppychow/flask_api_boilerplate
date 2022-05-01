import json
from flask import jsonify, request
from marshmallow import ValidationError
from sqlalchemy.exc import InvalidRequestError

from app import db
from models.dog import Dog
from schemas.dog_schema import dog_schema, dogs_schema


class DogController:
    @classmethod
    def index(cls):
        try:
            dogs = Dog.query.filter_by(**request.args).all()
            return jsonify(dogs_schema.dump(dogs))
        except InvalidRequestError as err:
            return {"message": "Unable to find dogs based on filters entered."}, 500

    @classmethod
    def show(cls, dog_id):
        dog = Dog.query.get_or_404(dog_id)
        return jsonify(dog_schema.dump(dog))

    @classmethod
    def create(cls):
        try:
            data = dog_schema.load(request.json)
            new_dog = Dog(**data)
            db.session.add(new_dog)
            db.session.commit()
            return jsonify(dog_schema.dump(new_dog)), 201
        except ValidationError as err:
            return {'message': err.messages}, 400
        except Exception as err:
            return {"message": "Unable to create dog"}, 500

    @classmethod
    def update(cls, dog_id):
        try:
            data = dog_schema.load(request.json)
            Dog.query.filter_by(id=dog_id).update(data)
            db.session.commit()
            return {}, 204
        except ValidationError as err:
            return {'message': err.messages}, 400
        except Exception as err:
            return {"message": f"Unable to update dog: {dog_id}"}, 500


    @classmethod
    def delete(cls, dog_id):
        dog = Dog.query.get_or_404(dog_id)
        try:
            db.session.delete(dog)
            db.session.commit()
            return {"message": f"Successfully deleted dog: {dog_id}"}, 200
        except Exception as err:
            return {"message": f"Unable to delete dog: {dog_id}"}
