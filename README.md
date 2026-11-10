# ISMS Review Center

A standalone review dashboard and integration layer for the ISMS document-review workflow. This repository is intentionally separate from `document-review`.

## Scope

- Reviewer-facing dashboard and review workflow API.
- Integration with a **test** Linux server only.
- Receiving and tracking DOCX/JSON review artifacts.
- Reviewer assignment, decisions, and an auditable event trail.
- No production-server credentials or secrets committed to Git.

## Architecture (initial scaffold)

- `backend/`: Python API (FastAPI), health endpoint, and typed configuration.
- `frontend/`: reserved for the review dashboard UI.
- `services/`: reserved for test-server transfer/worker adapters.
- `tests/`: API and integration contract tests.
- `docs/`: integration contract and local development notes.

The server adapter is deliberately not implemented until the test server's transport, authentication, directory layout, and JSON schema are confirmed. This avoids guessing operational details.

## Quick start

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn backend.app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the API docs and `http://127.0.0.1:8000/health` for the health check.

## Configuration

See `.env.example`. Keep real credentials in an untracked local `.env` or deployment secret store. Never commit passwords, private keys, tokens, or real ISMS documents.

## Development principles

1. Keep test and production environments strictly separated.
2. Validate incoming filenames, file sizes, MIME types, and JSON schemas.
3. Treat transferred documents and metadata as untrusted input.
4. Record reviewer actions with actor and timestamp.
5. Do not mark a document approved merely because a file transfer succeeded.

## Status

Initial project scaffold. The concrete server integration contract and dashboard framework are pending confirmation.
