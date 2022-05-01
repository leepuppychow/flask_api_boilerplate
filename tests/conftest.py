import pytest
from app import create_app, db

from models.dog import Dog


@pytest.fixture()
def test_client():
    app = create_app('config.testing')

    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture()
def init_database():
    db.create_all()

    dog_1 = Dog(name="dog 1", age=1)
    dog_2 = Dog(name="dog 2", age=2)

    db.session.add_all([dog_1, dog_2])
    db.session.commit()

    yield

    db.session.remove()
    db.drop_all()
