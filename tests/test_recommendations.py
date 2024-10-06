# tests/test_recommendations.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_recommendations():
    # Basic test structure for the /recommendations endpoint
    response = client.post(
        "/recommendations",
        json={
            "user_id": "test_user",
            "preferences": ["test preference"]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "test_user"
    assert "recommendations" in data
    assert isinstance(data["recommendations"], list)
