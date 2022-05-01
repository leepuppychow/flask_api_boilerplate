from flask import jsonify, request

from app import db
from models.dog import Dog
from schemas.dog_schema import dog_schema, dogs_schema


class DogController:
    @classmethod
    def index(cls):
        dogs = Dog.query.filter_by(**request.args).all()
        return jsonify(dogs_schema.dump(dogs))

    @classmethod
    def show(cls, dog_id):
        dog = Dog.query.get_or_404(dog_id)
        return jsonify(dog_schema.dump(dog))

    @classmethod
    def create(cls):
        data = dog_schema.load(request.json)
        new_dog = Dog(**data)
        db.session.add(new_dog)
        db.session.commit()
        return jsonify(dog_schema.dump(new_dog)), 201

    @classmethod
    def update(cls, dog_id):
        data = dog_schema.load(request.json)
        Dog.query.filter_by(id=dog_id).update(data)
        db.session.commit()
        return {}, 204

    @classmethod
    def delete(cls, dog_id):
        dog = Dog.query.get_or_404(dog_id)
        db.session.delete(dog)
        db.session.commit()
        return {"message": f"Successfully deleted dog: {dog_id}"}, 200
