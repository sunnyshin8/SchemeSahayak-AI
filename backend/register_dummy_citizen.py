import requests

url = "http://localhost:8000/api/agency/register"
payload = {
    "citizen_id": "9999-8888-7777",
    "name": "Ramesh Gupta",
    "details": "Farmer seeking subsidy"
}

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Successfully registered dummy citizen: Ramesh Gupta")
    else:
        print(f"Failed to register. Status: {response.status_code}, Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
