# Project 2: Gym Member Grouping
# Unsupervised Learning using KMeans

import numpy as np
from sklearn.cluster import KMeans

# Step 1: Create dataset with at least 8 members
# Features: [Age, Monthly Gym Visits]
# No labels needed for unsupervised learning!

gym_members =np.array([
    [22, 20],   # Member 1: 22 years old, 20 visits/month
    [25, 18],   # Member 2 
    [45, 5],    # Member 3
    [50, 4],    # Member 4
    [30, 15],   # Member 5
    [28, 22],   # Member 6
    [48, 6],    # Member 7
    [35, 12],   # Member 8
    [23, 25],   # Member 9
    [55, 3],    # Member 10
])

# Step 2: Create KMeans model with n_clusters=2 or 3
gym_members_model= KMeans(n_clusters=2, random_state=42, n_init=10)

#training the model
gym_members_model.fit(gym_members)

# Step 3: Display cluster labels for training data

#view the results
print(gym_members_model.labels_)

# Step 4: Predict clusters for at least 2 new members
new_members = [
    [24, 19],   # New Member 1
    [47, 5],    # New Member 2
    [33, 14],   # New Member 3 (bonus)
]
print(gym_members_model.predict([[24,19]]))





