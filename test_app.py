import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    """Test endpointu monitorowania stanu aplikacji (/health)"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_index_endpoint(client):
    """Test odpowiedzi strony głównej"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["status"] == "success"
