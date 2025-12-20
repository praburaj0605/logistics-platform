from fastapi import FastAPI
from app.api import auth, clients, enquiries, vendors, ratecards, quotes, orders, shipments


app = FastAPI(title="Logistics Platform API")

app.include_router(auth.router)
app.include_router(clients.router)
app.include_router(enquiries.router)
app.include_router(vendors.router)
app.include_router(ratecards.router)
app.include_router(quotes.router)
app.include_router(orders.router)
app.include_router(shipments.router)


@app.get("/health")
def health():
    return {"status": "ok"}
