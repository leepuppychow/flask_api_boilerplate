from app import db
from models.dog import Dog


class TestDogEndpoints:
    def test_index(self, test_client, init_database):
        response = test_client.get('/api/v1/dogs/')

        assert response.status_code == 200
        assert len(response.json) == 2

    def test_show(self, test_client, init_database):
        doggo = Dog(id=100, name="Tobi", age=16)
        db.session.add(doggo)
        db.session.commit()

        response = test_client.get(f'/api/v1/dogs/{doggo.id}')

        assert response.status_code == 200
        assert response.json['id'] == doggo.id
        assert response.json['age'] == doggo.age
        assert response.json['name'] == doggo.name

    def test_show_not_found(self, test_client, init_database):
        response = test_client.get(f'/api/v1/dogs/99999')

        assert response.status_code == 404

    def test_create_success(self, test_client, init_database):
        payload = {
            "name": "super doggo",
            "age": 20
        }
        response = test_client.post('/api/v1/dogs/', json=payload)

        assert response.status_code == 201

    def test_create_missing_name(self, test_client, init_database):
        payload = {
            "name": None,
            "age": 20
        }
        response = test_client.post('/api/v1/dogs/', json=payload)

        assert response.status_code == 400
        assert response.json == {'message': {'name': ['Field may not be null.']}}

    def test_create_invalid_age(self, test_client, init_database):
        payload = {
            "name": "Dug",
            "age": "not an int"
        }
        response = test_client.post('/api/v1/dogs/', json=payload)

        assert response.status_code == 400
        assert response.json == {'message': {'age': ['Not a valid integer.']}}

    def test_update_success(self, test_client, init_database):
        doggo = Dog(id=100, name="Tobi", age=16)
        db.session.add(doggo)
        db.session.commit()

        payload = {
            "name": "TOBI",
            "age": 17,
        }
        response = test_client.put(f'/api/v1/dogs/{doggo.id}', json=payload)

        assert response.status_code == 204

        tobi = Dog.query.get(doggo.id)
        
        assert tobi.name == "TOBI"
        assert tobi.age == 17

    def test_delete_success(self, test_client, init_database):
        doggo = Dog(id=100, name="Tobi", age=16)
        db.session.add(doggo)
        db.session.commit()

        response = test_client.delete(f'/api/v1/dogs/{doggo.id}')

        assert response.status_code == 200

        tobi = Dog.query.get(doggo.id)
        assert not tobi

    def test_delete_not_found(self, test_client, init_database):
        response = test_client.delete('/api/v1/dogs/9999')

        assert response.status_code == 404
