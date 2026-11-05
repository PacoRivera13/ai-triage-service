from fastapi import FastAPI

app = FastAPI(title="ai-triage-service")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
