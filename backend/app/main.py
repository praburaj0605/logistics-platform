from fastapi import FastAPI
from app.api import auth
from app.api import clients


app = FastAPI(title="Logistics Platform API")

app.include_router(auth.router)
app.include_router(clients.router)

@app.get("/health")
def health():
    return {"status": "ok"}
