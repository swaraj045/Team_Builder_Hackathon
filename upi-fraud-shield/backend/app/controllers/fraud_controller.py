from app.services import receiver_risk_service

def get_receiver_risk(receiver_upi: str):

    risk_data = receiver_risk_service.check_receiver(receiver_upi)

    return {
        "receiver_upi": receiver_upi,
        "risk_score": risk_data["risk_score"],
        "status": risk_data["status"],
        "complaints": risk_data["complaints"]
    }