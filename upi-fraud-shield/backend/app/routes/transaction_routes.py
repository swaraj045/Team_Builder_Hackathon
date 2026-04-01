from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.schemas.transaction_schema import TransactionInitiate
from app.controllers import transaction_controller

router = APIRouter(
    prefix="/transaction",
    tags=["Transactions"]
)


# 1️⃣ Initiate Transaction
@router.post("/initiate")
def initiate_transaction(
    data: TransactionInitiate,
    db: Session = Depends(get_db)
):
    return transaction_controller.initiate_transaction(data, db)


# 2️⃣ Verify PIN (moves to PIN_VERIFIED state)
@router.post("/verify-pin")
def verify_pin(
    transaction_id: str = Query(...),
    db: Session = Depends(get_db)
):
    return transaction_controller.verify_pin(transaction_id, db)


# 3️⃣ Run AI Review Layer (Post-PIN Security Check)
@router.post("/ai-review")
def ai_review(
    transaction_id: str = Query(...),
    db: Session = Depends(get_db)
):
    return transaction_controller.ai_review(transaction_id, db)
