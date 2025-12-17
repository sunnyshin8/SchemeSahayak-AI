from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

# Mock Data
CITIZEN_SEARCH_PAYLOAD = {"query": "I need a loan for farming"}
AGENCY_VERIFY_PAYLOAD = {
    "citizen_id": "9999-8888-7777",
    "name": "Ramesh Gupta",
    "details": "Farmer seeking subsidy"
}
AGENCY_TOKEN = "Bearer agency-secret-123"

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "SchemeSahayak Backend" in response.json()["message"]

def test_search_schemes():
    response = client.post("/api/citizen/search", json=CITIZEN_SEARCH_PAYLOAD)
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    # Mock DB should return some results
    # assert len(data["results"]) > 0 

def test_agency_verification_unauthorized():
    response = client.post("/api/agency/verify", json=AGENCY_VERIFY_PAYLOAD)
    # Should fail without token
    assert response.status_code == 401

def test_agency_verification_authorized():
    headers = {"Authorization": AGENCY_TOKEN}
    response = client.post("/api/agency/verify", json=AGENCY_VERIFY_PAYLOAD, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "is_fraud" in data

def test_cors_preflight():
    response = client.options("/api/citizen/search")
    assert response.status_code == 200
