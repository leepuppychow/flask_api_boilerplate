from app import db


class TestSampleEndpoints:
    def test_index(self, test_client, init_database):
        response = test_client.get('/api/v1/samples')

        assert response.status_code == 200
        assert response.json
