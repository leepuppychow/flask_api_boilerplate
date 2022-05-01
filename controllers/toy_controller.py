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
        toys = Toy.query.filter(Toy.dog==dog).all()
        return jsonify(toys_schema.dump(toys)), 200
    
    @classmethod
    def create(cls, dog_id):
        dog = cls.get_dog(dog_id)
        validated_data = toys_schema.load(request.json)
        new_toys = []
        for toy_data in validated_data:
            new_toy = Toy(**toy_data, dog=dog)
            db.session.add(new_toy)
            new_toys.append(new_toy)
        
        db.session.commit()
        return jsonify(toys_schema.dump(new_toys)), 201