from app.middleware import ai_review_layer

def ai_review(data):

    transaction_id = data.get("transaction_id")

    if transaction_id not in transactions:
        return {"error": "Transaction not found"}

    transaction = transactions[transaction_id]

    review_result = ai_review_layer.run_ai_review(transaction)

    decision = review_result["decision"]

    if decision == "BLOCK":
        transactions[transaction_id]["status"] = "BLOCKED"
        message = "Transaction Blocked - High Fraud Risk"

    elif decision == "WARNING":
        transactions[transaction_id]["status"] = "WARNING"
        message = "Suspicious Transaction - User Confirmation Required"

    else:
        transactions[transaction_id]["status"] = "COMPLETED"
        message = "Transaction Successful"

    return {
        "transaction_id": transaction_id,
        "risk_score": review_result["final_risk_score"],
        "receiver_status": review_result["receiver_status"],
        "status": transactions[transaction_id]["status"],
        "message": message
    }
