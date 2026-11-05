# ai-triage-service

A FastAPI service that will triage support tickets using Claude with tool calling, and track token usage and cost for every request.

> **Status: early development.** Only the project foundation exists so far: settings, an app with a `/health` route, and tests. Triage isn't built yet.

## Roadmap

- [x] M1. Project foundation
- [ ] M2. Cost calculator
- [ ] M3. The three tools (`lookup_customer`, `search_knowledge_base`, `get_ticket_history`)
- [ ] M4. First model call
- [ ] M5. The tool loop
- [ ] M6. Usage logging in SQLite
- [ ] M7. API endpoints (`POST /triage`, `GET /usage/summary`)
- [ ] M8. First run against the real API
- [ ] M9. Full documentation and CI

## Requirements

- [uv](https://docs.astral.sh/uv/), which installs Python 3.12 for this project if needed

## Setup

```bash
uv sync
cp .env.example .env
```

No API key is needed yet. Nothing calls the Claude API at this stage, and `.env` is ignored by git.

## Run

```bash
uv run uvicorn app.main:app --reload
```

Then open <http://127.0.0.1:8000/health>, which should return `{"status":"ok"}`. Interactive API docs are at <http://127.0.0.1:8000/docs>.

## Test

```bash
uv run ruff check .
uv run pytest
```

Tests don't need an API key.
