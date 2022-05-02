import pytest
from app import create_app, db

@pytest.fixture()
def test_client():
    app = create_app('config.testing')

    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture()
def init_database():
    db.create_all()

    # Can create some seed data save to DB here:

    db.session.commit()

    yield

    db.session.remove()
    db.drop_all()
