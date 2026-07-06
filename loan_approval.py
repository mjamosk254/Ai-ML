import tensorflow as tf
import numpy as np

# Assignment 9: Binary Classification - Loan Approval System
# A bank wants to build an AI system that determines whether a customer qualifies for a loan.
# Input features (4 features per customer):
#   - Monthly Income
#   - Credit Score
#   - Years of Employment
#   - Existing Debt
#
# Output labels:
#   - 0 = Reject
#   - 1 = Approve

# STEP 1: Creating the Training Dataset
# Each row represents one customer: [Monthly Income, Credit Score, Years of Employment, Existing Debt]
# Label: 0 = Reject, 1 = Approve

# Training data (12 examples)
# Higher income, higher credit score, more years employed, lower debt = more likely to be approved
x = np.array([
    # [Monthly Income, Credit Score, Years of Employment, Existing Debt]
    [35000,  580, 1, 25000],   # Low income, low credit, new employee, high debt  -> Reject
    [42000,  610, 2, 20000],   # Low income, low credit, short tenure, high debt  -> Reject
    [38000,  550, 1, 30000],   # Low income, poor credit, new, very high debt     -> Reject
    [45000,  620, 2, 22000],   # Below average across board                       -> Reject
    [55000,  680, 3, 15000],   # Moderate income, fair credit, moderate debt      -> Reject
    [60000,  700, 4, 12000],   # Borderline case                                  -> Reject
    [72000,  740, 5, 10000],   # Good income, good credit, stable employment       -> Approve
    [85000,  760, 6, 8000],    # Strong profile                                    -> Approve
    [95000,  790, 8, 5000],    # High income, excellent credit, long tenure        -> Approve
    [110000, 820, 10, 4000],   # Very strong profile                               -> Approve
    [125000, 850, 12, 2000],   # Excellent profile                                 -> Approve
    [150000, 900, 15, 0],      # Outstanding profile                               -> Approve
], dtype=np.float32)

# Labels: 0 = Reject, 1 = Approve
y = np.array([
    0,  # Reject
    0,  # Reject
    0,  # Reject
    0,  # Reject
    0,  # Reject
    0,  # Reject
    1,  # Approve
    1,  # Approve
    1,  # Approve
    1,  # Approve
    1,  # Approve
    1,  # Approve
], dtype=np.float32)

# STEP 2: Building the Neural Network
# Architecture (following the pattern from tensor_project2.py):
#   - Input layer: 4 features (automatically inferred)
#   - 1st Hidden layer: 16 neurons, ReLU activation
#   - 2nd Hidden layer: 8 neurons, ReLU activation
#   - Output layer: 1 neuron, Sigmoid activation (for binary classification)

model = tf.keras.Sequential([
    # 1st Hidden Layer
    tf.keras.layers.Dense(16, activation="relu", input_shape=(4,)),

    # 2nd Hidden Layer
    tf.keras.layers.Dense(8, activation="relu"),

    # Output Layer (Binary Classification)
    # Sigmoid outputs a probability between 0 and 1
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# STEP 3: Compiling the Model
# For Binary Classification:
#   - Loss function: binary_crossentropy (standard for binary classification)
#   - Optimizer: adam (adaptive learning rate, works well in most cases)
#   - Metrics: accuracy (to monitor performance)

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# STEP 4: Training the Model
history = model.fit(x, y, epochs=100, verbose=1)

# STEP 5: Making a Prediction for a New Customer
# New customer: [Monthly Income, Credit Score, Years of Employment, Existing Debt]
# Example: Customer with $120,000 income, 780 credit score, 8 years employed, $15,000 debt

new_customer = np.array([[120000, 780, 8, 15000]], dtype=np.float32)
prediction = model.predict(new_customer, verbose=0)
probability = prediction[0][0]

print(prediction)