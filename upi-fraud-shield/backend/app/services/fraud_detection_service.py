# Example fraud database
blacklisted_receivers = [
    "fraud@upi",
    "scammer@upi"
]

# Simulated user behavior
average_transaction_amount = 2000


def calculate_risk(transaction):

    risk_score = 0

    receiver = transaction["receiver"]
    amount = transaction["amount"]

    # Rule 1: Receiver blacklist check
    if receiver in blacklisted_receivers:
        risk_score += 80

    # Rule 2: High transaction amount
    if amount > average_transaction_amount * 3:
        risk_score += 30

    # Rule 3: First time receiver (simulated)
    if receiver not in ["friend@upi", "family@upi"]:
        risk_score += 20

    return risk_score