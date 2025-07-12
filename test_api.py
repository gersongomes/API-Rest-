from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_dado_existente():
    response = client.get("/dados/1")
    assert response.status_code == 200
    assert "titulo" in response.json()

def test_get_dado_inexistente():
    response = client.get("/dados/999")
    assert response.status_code == 404
    assert response.json() == {"erro": "Dado não encontrado"}
