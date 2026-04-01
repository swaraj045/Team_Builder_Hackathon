import numpy as np


def extract_features(transaction, user_profile):
    """
    Convert transaction data into feature vector
    """

    amount = transaction["amount"]
    receiver = transaction["receiver"]
    hour = transaction.get("hour", 12)

    avg_amount = user_profile["avg_transaction"]

    # Feature 1: Amount ratio
    amount_ratio = amount / avg_amount

    # Feature 2: Is new receiver
    is_new_receiver = 1 if receiver not in user_profile["known_receivers"] else 0

    # Feature 3: Odd hour flag
    is_odd_hour = 1 if hour < 8 or hour > 22 else 0

    return np.array([
        amount_ratio,
        is_new_receiver,
        is_odd_hour
    ])