import requests
import json
import time

BASE_URL = "http://localhost:8000/api/auth"

def test_register():
    print("Testing Registration...")
    email = f"test_{int(time.time())}@example.com"
    payload = {
        "name": "Test User",
        "email": email,
        "password": "password123"
    }
    try:
        response = requests.post(f"{BASE_URL}/register", json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        return email
    except Exception as e:
        print(f"Registration Failed: {e}")
        return None

def test_login(email):
    print("\nTesting Login...")
    payload = {
        "email": email,
        "password": "password123"
    }
    try:
        response = requests.post(f"{BASE_URL}/login", json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Login Failed: {e}")

if __name__ == "__main__":
    email = test_register()
    if email:
        test_login(email)
