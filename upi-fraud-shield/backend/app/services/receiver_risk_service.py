# Simulated fraud database
fraud_database = {
    "fraud@upi": {
        "complaints": 15,
        "risk_score": 85
    },
    "scammer@upi": {
        "complaints": 8,
        "risk_score": 70
    }
}

def check_receiver(receiver_upi: str):

    if receiver_upi in fraud_database:
        data = fraud_database[receiver_upi]

        return {
            "complaints": data["complaints"],
            "risk_score": data["risk_score"],
            "status": "HIGH_RISK"
        }

    return {
        "complaints": 0,
        "risk_score": 10,
        "status": "TRUSTED"
    }