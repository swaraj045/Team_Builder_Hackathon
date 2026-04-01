import time
from typing import Dict

from app.services import fraud_detection_service
from app.services import receiver_risk_service


# -------------------------------
# CONFIGURATION
# -------------------------------

AI_REVIEW_DELAY_SECONDS = 10      # Change to 3 for faster testing
MAX_RISK_SCORE = 100


# -------------------------------
# CORE AI REVIEW FUNCTION
# -------------------------------

def run_ai_review(transaction: Dict) -> Dict:
    """
    Post-PIN Intelligent Verification Layer

    Runs after PIN verification and before final settlement.
    Combines:
    - Behavioral anomaly detection
    - Receiver intelligence scoring
    - Risk normalization
    - Final decision logic
    """

    # 🔒 Simulate intelligent review window (micro-intervention delay)
    time.sleep(AI_REVIEW_DELAY_SECONDS)

    total_risk_score = 0

    # -----------------------------------
    # 1️⃣ Behavioral Risk Evaluation
    # -----------------------------------
    behavioral_risk = fraud_detection_service.calculate_risk(transaction)
    total_risk_score += behavioral_risk

    # -----------------------------------
    # 2️⃣ Receiver Risk Intelligence
    # -----------------------------------
    receiver_data = receiver_risk_service.check_receiver(
        transaction["receiver"]
    )

    # Weighted receiver influence (50%)
    receiver_weighted_risk = receiver_data["risk_score"] * 0.5
    total_risk_score += receiver_weighted_risk

    # -----------------------------------
    # 3️⃣ Normalize Risk Score
    # -----------------------------------
    if total_risk_score > MAX_RISK_SCORE:
        total_risk_score = MAX_RISK_SCORE

    final_score = int(total_risk_score)

    # -----------------------------------
    # 4️⃣ Decision Engine
    # -----------------------------------
    if final_score >= 70:
        decision = "BLOCK"
        explanation = "High probability of fraud detected."
    elif final_score >= 40:
        decision = "WARNING"
        explanation = "Transaction appears unusual."
    else:
        decision = "ALLOW"
        explanation = "Transaction appears safe."

    # -----------------------------------
    # 5️⃣ Return Structured Response
    # -----------------------------------
    return {
        "final_risk_score": final_score,
        "decision": decision,
        "receiver_status": receiver_data["status"],
        "behavioral_risk": behavioral_risk,
        "receiver_risk": receiver_data["risk_score"],
        "explanation": explanation
    }
