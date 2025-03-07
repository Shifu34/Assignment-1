import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert "message" in json_data
    assert json_data["message"] == "Welcome to the ML CI/CD Pipeline Demo!"
