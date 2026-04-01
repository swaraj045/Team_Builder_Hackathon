from sqlalchemy.orm import Session
from app.models.transaction_model import Transaction
from app.middleware import ai_review_layer


def initiate_transaction(data, db: Session):

    new_tx = Transaction(
        transaction_id=data.transaction_id,
        sender=data.sender,
        receiver=data.receiver,
        amount=data.amount,
        status="INITIATED"
    )

    db.add(new_tx)
    db.commit()
    db.refresh(new_tx)

    return {
        "transaction_id": new_tx.transaction_id,
        "status": new_tx.status
    }


def verify_pin(transaction_id: str, db: Session):

    tx = db.query(Transaction).filter(
        Transaction.transaction_id == transaction_id
    ).first()

    if not tx:
        return {"error": "Transaction not found"}

    tx.status = "PIN_VERIFIED"
    db.commit()

    return {
        "transaction_id": tx.transaction_id,
        "status": tx.status
    }


def ai_review(transaction_id: str, db: Session):

    tx = db.query(Transaction).filter(
        Transaction.transaction_id == transaction_id
    ).first()

    if not tx:
        return {"error": "Transaction not found"}

    transaction_data = {
        "receiver": tx.receiver,
        "amount": tx.amount
    }

    review_result = ai_review_layer.run_ai_review(transaction_data)

    tx.risk_score = review_result["final_risk_score"]

    if review_result["decision"] == "BLOCK":
        tx.status = "BLOCKED"
        message = "Transaction Blocked - High Fraud Risk"

    elif review_result["decision"] == "WARNING":
        tx.status = "WARNING"
        message = "Suspicious Transaction - User Confirmation Required"

    else:
        tx.status = "COMPLETED"
        message = "Transaction Successful"

    db.commit()

    return {
        "transaction_id": tx.transaction_id,
        "risk_score": tx.risk_score,
        "receiver_status": review_result["receiver_status"],
        "status": tx.status,
        "message": message
    }
