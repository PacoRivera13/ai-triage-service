# Project: ai-triage-service
Python 3.12 FastAPI service that triages support tickets using Claude with tool calling.

## Conventions
- Type hints everywhere; pydantic models for all request/response shapes
- Pricing lives in `pricing.json`, never hardcoded in logic
- Tests must never call the real API; mock the client
- Run `ruff check . && pytest` before every commit
- Small commits, one per stage
- Explain Python-specific idioms briefly when you use them (I'm a senior .NET dev learning Python)
