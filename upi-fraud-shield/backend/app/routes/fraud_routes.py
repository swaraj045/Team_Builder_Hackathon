from fastapi import APIRouter
from app.controllers import fraud_controller

router = APIRouter(prefix="/fraud", tags=["Fraud"])

@router.get("/receiver-risk/{receiver_upi}")
def get_receiver_risk(receiver_upi: str):
    return fraud_controller.get_receiver_risk(receiver_upi)