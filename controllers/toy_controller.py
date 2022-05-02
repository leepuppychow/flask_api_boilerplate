from flask import jsonify, request

from app import db
from models.dog import Dog
from models.toy import Toy

from schemas.toy_schema import toy_schema, toys_schema


class ToyController:
    @classmethod
    def get_dog(cls, dog_id):
        return Dog.query.get_or_404(dog_id)

    @classmethod
    def index(cls, dog_id):
        dog = cls.get_dog(dog_id)
        return jsonify(toys_schema.dump(dog.toys)), 200
    
    @classmethod
    def create(cls, dog_id):
        dog = cls.get_dog(dog_id)
        validated_data = toys_schema.load(request.json)
        for toy_data in validated_data:
            dog.toys.append(Toy(**toy_data))
        db.session.commit()
        return jsonify(toys_schema.dump(dog.toys)), 201