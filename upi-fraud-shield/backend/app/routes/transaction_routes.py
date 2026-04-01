from fastapi import APIRouter
from app.controllers import transaction_controller

router = APIRouter(prefix="/transaction", tags=["Transactions"])

@router.post("/initiate")
def initiate_transaction(data: dict):
    return transaction_controller.initiate_transaction(data)

@router.post("/verify-pin")
def verify_pin(data: dict):
    return transaction_controller.verify_pin(data)

@router.post("/ai-review")
def ai_review(data: dict):
    return transaction_controller.ai_review(data)