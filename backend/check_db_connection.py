
from database import get_cyborg_client, MockCyborgClient
import os

print("Checking DB Client...")
c = get_cyborg_client()

if isinstance(c, MockCyborgClient):
    print("RESULT: USING MOCK CLIENT")
else:
    print("RESULT: USING REAL CLIENT")
    try:
        idx = c.get_index("schemes")
        print(f"Index retrieved: {idx}")
        print("RESULT: REAL CONNECTION OK")
    except Exception as e:
        print(f"RESULT: REAL CONNECTION ERROR: {e}")
