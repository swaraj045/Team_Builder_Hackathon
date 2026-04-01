from fastapi import FastAPI
from app.routes import transaction_routes

app = FastAPI(
    title="UPI Fraud Shield API",
    description="Post-PIN Intelligent Fraud Prevention Layer",
    version="1.0"
)

# Include routes
app.include_router(transaction_routes.router)

@app.get("/")
def read_root():
    return {"message": "UPI Fraud Shield API Running"}