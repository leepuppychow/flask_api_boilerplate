import pytest
from app import create_app, db


@pytest.fixture
def test_client(scope="module"):
    app = create_app('config.testing')

    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture
def init_database(generate_dog, scope="module"):
    db.create_all()

    dog_1 = generate_dog(name="dog 1", age=1)
    dog_2 = generate_dog(name="dog 2", age=2)

    db.session.add_all([dog_1, dog_2])
    db.session.commit()

    yield

    db.session.remove()
    db.drop_all()

@pytest.fixture
def generate_dog(scope="module"):
    def _generate_dog(*args, **kwargs):
        from models.dog import Dog

        return Dog(**kwargs)

    return _generate_dog
