import pickle
import numpy as np
from ai_engine.features.feature_extraction import extract_features

# Load model
with open("ai-engine/models/anomaly_detector.pkl", "rb") as f:
    model = pickle.load(f)


# Simulated user profile
user_profile = {
    "avg_transaction": 2000,
    "known_receivers": ["friend@upi", "family@upi"]
}


def predict_risk(transaction):

    features = extract_features(transaction, user_profile)
    features = features.reshape(1, -1)

    prediction = model.predict(features)  # -1 = anomaly, 1 = normal

    if prediction[0] == -1:
        return 70  # high risk
    else:
        return 20  # low risk