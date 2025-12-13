from fastapi import FastAPI

app = FastAPI(title="Logistics Platform API")

@app.get("/health")
def health():
    return {"status": "ok"}
