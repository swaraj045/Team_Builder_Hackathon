import time
from app.services import fraud_detection_service
from app.services import receiver_risk_service

def run_ai_review(transaction):

    # Simulate AI review delay
    time.sleep(3)  # change to 10 for real demo

    total_risk = 0

    behavioral_risk = fraud_detection_service.calculate_risk(transaction)
    total_risk += behavioral_risk

    receiver_data = receiver_risk_service.check_receiver(transaction["receiver"])
    total_risk += receiver_data["risk_score"] * 0.5

    if total_risk > 100:
        total_risk = 100

    if total_risk >= 70:
        decision = "BLOCK"
    elif total_risk >= 40:
        decision = "WARNING"
    else:
        decision = "ALLOW"

    return {
        "final_risk_score": int(total_risk),
        "decision": decision,
        "receiver_status": receiver_data["status"]
    }
