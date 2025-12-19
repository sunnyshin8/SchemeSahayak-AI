## HackerEarth Username
@shingloo93 (Team: AiTron)

## Category
- [ ] Performance/Latency
- [ ] Integration (LangChain/LlamaIndex/other frameworks)
- [ ] Deployment (Kubernetes/Serverless/other)
- [ ] Compliance/Security
- [ ] Documentation
- [ ] Bug/Crash
- [x] Other: Feature Request / DevEx

## Description
**Feature Request for "Native Offline Adapter" & Report of Blocking Dependency Conflict.**

While developing *SchemeSahayak*, we faced significant friction due to a hard blocking issue where `urllib3` (v2.0.7) conflicts prevented the CyborgDB Python SDK from connecting to `api.cyborgdb.co`. The "door" to the server was effectively stuck due to library mismatches in our environment.

In a hackathon or rapid-prototyping environment, developers often need to:
1.  Work offline or with flaky internet.
2.  Run unit tests without hitting a remote API (speed/cost).
3.  Avoid complex dependency trees just to test basic vector ingestion logic.

Because the SDK defaults to a cloud-first connection, and failed when valid API keys weren't present or dependencies clashed, we were completely blocked until we implemented a custom "Offline Client" workaround. We request a native **Offline Adapter** in the SDK to allow local development without network reliance.

## Expected Behavior
We expect to be able to initialize the CyborgDB client in a local/offline mode that does not attempt any network connections.

**Desired Code:**
```python
import cyborgdb
# Initialize with offline adapter - no network calls, local storage only
client = cyborgdb.Client(adapter="offline", storage_path="./.cyborg_data")
index = client.create_index("test-index")
index.upsert(...) # Writes to local JSON/Parquet
```

## Actual Behavior
1.  **Dependency Conflict**: initializing `Client()` with `urllib3==2.0.7` installed raised connection errors (`urllib3` version conflict), preventing simple "Hello World" usage.
2.  **No Fallback**: There is no built-in way to say "just run locally" to bypass the connection check. The SDK crashed, blocking development.

## Reproduction Steps
1.  Set up a Python environment with `urllib3==2.0.7` (common in many modern stacks).
2.  Install `cyborgdb` SDK.
3.  Attempt to initialize `cyborgdb.Client("https://api.cyborgdb.co", "API_KEY")`.
4.  **Result**: Initialization fails/crashes due to `urllib3` incompatibility, or `ConnectionError` if offline.

## Environment Details
- **CyborgDB version:** Latest Python SDK
- **Deployment type:** Embedded / Local Dev
- **Backing store:** Memory / JSON (Mock)
- **OS:** Windows
- **Framework (if applicable):** FastAPI
- **Other relevant details:** `urllib3` version 2.0.7 caused the specific conflict.

## Performance Data (if applicable)
N/A (DevEx issue)

## Impact Assessment
**Critical / High.**
-   **Blocked Progress**: Initial setup cost ~2 hours of debugging dependency hell (`urllib3` downgrades) before we could even run the app.
-   **Duplicated Effort**: We had to write our own `OfflineEncryptedIndex` class to simulate the DB just to write unit tests.
-   **Barrier to Entry**: New users facing dependency errors might just abandon the tool if they can't test it offline first.

## Additional Context
We successfully resolved the immediate crash by forcing a downgrade to `urllib3<2.0.0` (specifically 1.26.20), but this should not be required for basic testing.

**Our Workaround (Custom Offline Adapter):**
To proceed, we had to implement this wrapper in our `database.py`:

```python
class OfflineEncryptedIndex:
    def __init__(self, name):
        self.filename = f"offline_index_{name}.json" 
        self.data = self._load() # Load from local JSON

    def upsert(self, items):
        # ... store vectors locally ...
        self._save()
```
We believe this functionality should be native to the SDK.
