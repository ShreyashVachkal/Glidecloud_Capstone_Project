from fastapi.testclient import TestClient
from app.server import app

client = TestClient(app)

def test_summarize_no_input():
    response = client.post("/summarize")
    assert response.status_code == 422
