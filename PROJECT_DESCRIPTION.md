# Project Name: SchemeSahayak

**Team Name:** AiTron
**Tagline:** AI-Powered Government Scheme Intelligence & Zero-Trust Verification Platform

## Problem Statement

In the current landscape of public welfare:
1.  **Information Asymmetry:** Citizens, especially in rural areas, struggle to navigate the complex web of over 800+ government schemes. They often rely on middlemen or lack awareness of benefits they are entitled to.
2.  **Leakage & Fraud:** Government agencies face significant challenges in detecting "double-dipping" or duplicate beneficiaries across different ministries due to siloed databases and privacy concerns preventing direct data sharing.
3.  **Connectivity Barriers:** Field agents often operate in low-connectivity zones, making cloud-only digital tools unreliable.

## Objective

Our objective is to bridge the gap between citizens and government benefits while ensuring the integrity of welfare distribution.
1.  **For Citizens:** Provide a "Sahayak" (Helper) that simplifies scheme discovery using natural language and supports local Indian languages.
2.  **For Agencies:** enable a **Zero-Trust Inter-Agency Verification** system that allows ministries to check for duplicate beneficiaries (fraud) without ever exposing or sharing raw PII (Personally Identifiable Information), leveraging **CyborgDB's Encrypted Vector Search**.

## Project Details

SchemeSahayak is a dual-interface platform:

### 1. Citizen Intelligence Module (Public Facing)
-   **Natural Language Search:** Citizens can type queries like "I am a farmer needing a loan for seeds" or "Scholarship for OBC student" instead of keyword matching.
-   **Multilingual Support:** Designed to support Indian languages (Hindi, etc.) to reach the grassroots level.
-   **AI Chat Assistant:** An interactive assistant that helps users check eligibility and required documents.

### 2. Agency Verification Module (Restricted)
-   **Privacy-Preserving De-Duplication:** Agencies can upload beneficiary profiles which are converted into encrypted vectors.
-   **Cross-Ministry Checks:** Detect if a beneficiary claiming a benefit in Scheme A has already claimed a conflicting benefit in Scheme B, without either agency viewing the other’s raw database.
-   **Dashboard:** Visual analytics of scheme performance and fraud detection metrics.

## Built With

-   **Frontend**: `Next.js 15`, `React 19`, `Tailwind CSS 4`
-   **Backend**: `FastAPI`, `Uvicorn`, `Python`
-   **AI & ML**: `SentenceTransformers` (all-MiniLM-L6-v2), `PyTorch`
-   **Database**: `CyborgDB` (Vector Database), `Redis` (Caching), `PostgreSQL` (Metadata - Optional)
-   **DevOps**: `Docker`

## Instructions

### Prerequisites
-   Python 3.9+
-   Node.js 18+

### Installation & Running

1.  **Start Backend (FastAPI)**
    ```bash
    cd backend
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    python main.py
    ```
    *Server currently runs on port 8000.*

2.  **Start Frontend (Next.js)**
    ```bash
    cd frontend
    npm install
    npm run dev
    ```
    *Application runs on http://localhost:3000*

3.  **Authentication (Optional)**
    -   To use real CyborgDB, add `CYBORGDB_API_KEY` to `.env`.
    -   By default, the system runs in "Local/Mock Mode" for easy evaluation.

### Testing
To verify performance:
```bash
python backend/benchmark.py
```

## Methodology

Our solution leverages **Retrieval-Augmented Generation (RAG)** and **Vector Database** technologies.

1.  **Data Ingestion:**
    -   We ingested 800+ government schemes (sourced from official datasets) into **CyborgDB**.
    -   Textual descriptions, eligibility criteria, and benefits were embedded using `SentenceTransformers`.

2.  **Search & Retrieval:**
    -   User queries are embedded into vectors.
    -   CyborgDB performs a semantic similarity search to find the most relevant schemes, ranking them by relevance score.

3.  **Zero-Trust Verification Architecture:**
    -   **Blind Indexing:** Beneficiary PII (Name, Aadhaar Hash, DOB) is tokenized and embedded into an encrypted vector space.
    -   **Verification:** When an agency queries a profile, the system checks for vector collision (high similarity) in the encrypted index. If a match is found, it flags potential fraud *without decrypting the identity*.

## Scope of the Solution

### Current MVP (Hackathon Submission)
-   **Fully Functional Search:** Indexing and semantic search for nearly 1000 schemes.
-   **Agency Portal:** Interface for registering and verifying beneficiaries.
-   **Mock Data Simulation:** We generated 1000 mock Indian citizen profiles to demonstrate the scale and performance of the de-duplication engine.
-   **Mobile Responsive UI:** Optimized for accessibility on basic smartphones.

### Future Roadmap
-   **Offline Edge Deployment:** Integrating a "Native Offline Adapter" (as proposed in our feedback) to allow field agents to work without internet.
-   **Voice Interface:** Adding Speech-to-Text for illiterate users.
-   **Blockchain Integration:** For immutable audit logs of benefit disbursements.

## Additional Relevant Details

-   **Hackathon Feedback Contribution:**
    -   We actively tested the CyborgDB Python SDK and provided a detailed technical report (see `CYBORGDB_FEEDBACK.md`) regarding `urllib3` conflicts and the critical need for a Native Offline Mode, which we patched with a custom adapter during development.
