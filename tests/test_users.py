# tests/test_users.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_user_recommendations():
    # Basic test structure for the /users/{user_id}/recommendations endpoint
    user_id = "test_user"
    response = client.get(f"/users/{user_id}/recommendations")
    if response.status_code == 200:
        data = response.json()
        assert data["user_id"] == user_id
        assert "recommendations" in data
        assert isinstance(data["recommendations"], list)
    elif response.status_code == 404:
        data = response.json()
        assert "error" in data
    else:
        assert False, "Unexpected status code"
