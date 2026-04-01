from fastapi import FastAPI
from app.routes import transaction_routes
from app.database.db_connection import engine
from app.models import transaction_model, user_model

transaction_model.Base.metadata.create_all(bind=engine)

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
