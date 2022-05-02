from flask import jsonify, request

from app import db
from models.dog import Dog
from models.park import Park

from schemas.park_schema import park_schema, parks_schema


class ParkController:
    @classmethod
    def get_dog(cls, dog_id):
        return Dog.query.get_or_404(dog_id)

    @classmethod
    def index(cls, dog_id):
        dog = cls.get_dog(dog_id)
        return jsonify(parks_schema.dump(dog.parks)), 200

    @classmethod
    def create(cls, dog_id):
        dog = cls.get_dog(dog_id)
        validated_data = parks_schema.load(request.json)
        for park_data in validated_data:
            existing_park_id = park_data.get('id')
            if existing_park_id:
                park = Park.query.get_or_404(existing_park_id)
            else:
                park = Park(**park_data)
            dog.parks.append(park)
        db.session.commit()
        return jsonify(parks_schema.dump(dog.parks)), 201
