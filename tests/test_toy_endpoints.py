from app import db
from models.dog import Dog
from models.toy import Toy


class TestToyEndpoints:
    def test_can_get_all_toys_for_a_dog(self, test_client, init_database):
        doggo = Dog(id=100, name="Tobi", age=16)
        toy_1 = Toy(name="wolfie", description="chomp chomp", dog=doggo)
        toy_2 = Toy(name="moosey", description="squeak squeak", dog=doggo)
        toy_3 = Toy(name="bone", description="crunch", dog=doggo)

        db.session.add(doggo)
        db.session.commit()

        response = test_client.get(f'/api/v1/dogs/{doggo.id}/toys')

        assert response.status_code == 200
        assert len(response.json) == 3

    def test_can_create_toys_for_a_dog(self, test_client, init_database):
        doggo = Dog(id=100, name="Tobi", age=16)
        db.session.add(doggo)
        db.session.commit()

        payload = [
            {
                "name": "wolfie"
            },
            {
                "name": "camel guy",
                "description": "I ate its eyes"
            }
        ]

        response = test_client.post(f"/api/v1/dogs/{doggo.id}/toys", json=payload)

        assert response.status_code == 201
        assert len(response.json) == 2

        doggo_toys = Toy.query.filter(Toy.dog == doggo).all()
        assert len(doggo_toys) == 2
        assert doggo_toys[0].name == "wolfie"
        assert doggo_toys[1].name == "camel guy"
    