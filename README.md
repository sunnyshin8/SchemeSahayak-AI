# SchemeSahayak

**AI-Powered Government Scheme Intelligence Platform**

SchemeSahayak enables citizens to discover government schemes using natural language ("I need a loan for farming") and allows agencies to perform secure, cross-ministry beneficiary verification to detect fraud without exposing sensitive data.

## Features

- **Citizen Intelligence Module**: Natural language search for 800+ schemes (Mock data seeded with 5 key schemes).
- **Inter-Agency Verification**: Encrypted/Vector-based profile matching to detect duplicate beneficiaries using CyborgDB (Mock/Simulated in MVP).
- **Privacy-First**: Zero-Trust architecture using vector embeddings.

## Tech Stack

- **Backend**: FastAPI, SentenceTransformers, CyborgDB (Real/Mock), Redis
- **Frontend**: Next.js 15, Tailwind CSS
- **Database**: CyborgDB (Encrypted Vector Search) or In-Memory Mock (Fallback)

## Security & Privacy (Hackathon Focus)

SchemeSahayak is built on a **Zero-Trust** architecture leveraging **CyborgDB's Encrypted Vector Search**. 

1.  **Vector Inversion Protection**: Traditional vector databases are susceptible to inversion attacks where original PII can be reconstructed from embeddings. CyborgDB ensures that stored vectors are encrypted and cannot be reversed to reveal citizen data.
2.  **Blind Indexing**: Beneficiary profiles are indexed as encrypted vectors. Inter-agency verification happens directly on these encrypted vectors without ever decrypting the underlying PII in the application layer.

## Benchmarks

We have included a `benchmark.py` script to validate performance. Preliminary results on local environment:

| Operation | Batch Size | Avg Time |
|-----------|------------|----------|
| Ingestion | 20 Schemes | ~0.005s/rec |
| Search    | 1 Query    | ~0.02s |
| Verify    | 1 Profile  | ~0.01s |

Run benchmarks yourself:
```bash
python backend/benchmark.py
```

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- (Optional) `CYBORGDB_API_KEY` in `.env` for real cloud database.

### Installation & Running

1. **Start Backend**
   ```bash
   cd backend
   # Create virtual env
   python -m venv venv
   .\venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Run Server
   python main.py
   ```
   *Runs on http://localhost:8000*

2. **Start Frontend**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   *Runs on http://localhost:3000*

## API Endpoints

- `POST /api/citizen/search`: Search schemes.
- `POST /api/agency/register`: Register incomplete beneficiary profile.
- `POST /api/agency/verify`: Check for duplicates/fraud.

## Project Structure

- `/backend`: FastAPI application and business logic.
- `/frontend`: Next.js web application.
- `/brain`: Project artifacts (Plans, Walkthroughs).

