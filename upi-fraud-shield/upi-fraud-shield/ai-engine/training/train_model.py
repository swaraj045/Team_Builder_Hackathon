import numpy as np
import pickle
from sklearn.ensemble import IsolationForest

# Fake training data (normal behavior)
# [amount_ratio, is_new_receiver, is_odd_hour]

X_train = np.array([
    [1.0, 0, 0],
    [0.8, 0, 0],
    [1.2, 0, 0],
    [0.5, 1, 0],
    [1.1, 0, 0],
    [0.9, 1, 0],
    [1.3, 0, 0],
])

# Train model
model = IsolationForest(contamination=0.2)
model.fit(X_train)

# Save model
with open("ai-engine/models/anomaly_detector.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")