import base64
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_response_success(monkeypatch):
    # Patch OpenAI call to avoid real API usage
    def fake_openai_response(image_bytes, prompt):
        return {"choices": [{"message": {"content": "fake reply"}}]}
    from app.utils import openai_service
    monkeypatch.setattr(openai_service, "get_openai_response_from_image", fake_openai_response)
    
    # Use a small dummy image
    dummy_image = base64.b64encode(b"testimage").decode()
    response = client.post("/api/v1/generate-response", json={
        "mood": "casual",
        "length": 1.0,
        "image_base64": dummy_image
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "data" in data

def test_generate_response_invalid_mood():
    dummy_image = base64.b64encode(b"testimage").decode()
    response = client.post("/api/v1/generate-response", json={
        "mood": "invalid",
        "length": 1.0,
        "image_base64": dummy_image
    })
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data

def test_generate_response_missing_image_base64():
    response = client.post("/api/v1/generate-response", json={
        "mood": "casual",
        "length": 1.0
    })
    assert response.status_code == 422  # FastAPI validation error for missing required field

def test_generate_response_missing_all_fields():
    response = client.post("/api/v1/generate-response", json={})
    assert response.status_code == 422  # FastAPI validation error

def test_generate_response_invalid_length():
    dummy_image = base64.b64encode(b"testimage").decode()
    response = client.post("/api/v1/generate-response", json={
        "mood": "casual",
        "length": 4.0,  # Invalid length
        "image_base64": dummy_image
    })
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data

def test_generate_response_empty_image_base64():
    response = client.post("/api/v1/generate-response", json={
        "mood": "casual",
        "length": 1.0,
        "image_base64": ""
    })
    assert response.status_code == 422  # FastAPI validation error for empty string 