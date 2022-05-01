from app import db

class TestDogEndpoints:
    def test_index(self, test_client, init_database):
        response = test_client.get('/api/v1/dogs/')

        assert response.status_code == 200
        assert len(response.json) == 2

    def test_show(self, test_client, init_database, generate_dog):
        doggo = generate_dog(id=100, name="Tobi", age=16)
        db.session.add(doggo)
        db.session.commit()

        response = test_client.get(f'/api/v1/dogs/{doggo.id}')

        assert response.status_code == 200
        assert response.json['id'] == doggo.id
        assert response.json['age'] == doggo.age
        assert response.json['name'] == doggo.name

    def test_create(self, test_client, init_database):
        pass