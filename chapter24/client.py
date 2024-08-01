from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

    headers = {"X-Token": "coneofsilence"}  # Correctly named and defined headers
    response = client.get("/items", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"test": "response coneofsilence"}

test_read_main()