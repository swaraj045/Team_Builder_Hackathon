from app.services import fraud_detection_service

# Simulated transaction storage
transactions = {}

def initiate_transaction(data):

    transaction_id = data.get("transaction_id")

    transactions[transaction_id] = {
        "receiver": data.get("receiver"),
        "amount": data.get("amount"),
        "status": "INITIATED"
    }

    return {
        "transaction_id": transaction_id,
        "status": "INITIATED"
    }


def verify_pin(data):

    transaction_id = data.get("transaction_id")

    if transaction_id not in transactions:
        return {"error": "Transaction not found"}

    transactions[transaction_id]["status"] = "PIN_VERIFIED"

    return {
        "transaction_id": transaction_id,
        "status": "PIN_VERIFIED"
    }


def ai_review(data):

    transaction_id = data.get("transaction_id")

    if transaction_id not in transactions:
        return {"error": "Transaction not found"}

    transaction = transactions[transaction_id]

    risk_score = fraud_detection_service.calculate_risk(transaction)

    if risk_score > 60:
        transactions[transaction_id]["status"] = "BLOCKED"
        result = "Transaction Blocked - High Fraud Risk"

    elif risk_score > 30:
        transactions[transaction_id]["status"] = "WARNING"
        result = "Suspicious Transaction - User Confirmation Required"

    else:
        transactions[transaction_id]["status"] = "COMPLETED"
        result = "Transaction Successful"

    return {
        "transaction_id": transaction_id,
        "risk_score": risk_score,
        "status": transactions[transaction_id]["status"],
        "message": result
    } 