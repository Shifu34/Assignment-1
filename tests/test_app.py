import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.app import app  # Now it should work


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
