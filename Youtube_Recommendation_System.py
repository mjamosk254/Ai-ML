import numpy as np

# Step 1: Create a list of YouTube content categories
youtube_categories = ["Technology", "Education", "Gaming", "Music", "Sports"]

# Step 2: Create a NumPy array showing how many times a user watched each category
watch_history = np.array([15, 8, 20, 5, 12])

# Step 3: Find the user's most watched category using NumPy
# Use np.argmax() to get the index of the highest watched category
top_index = np.argmax(watch_history)
# Convert the index to the actual category name
preferred_category = youtube_categories[top_index]

# Step 4: Calculate preference scores
# Total watched activities across all categories
total_watches = sum(watch_history)

# A dictionary to store preference strength for each category
scores = {}
for i in range(len(youtube_categories)):
    # Formula: preference_score = category_watches / total_watches
    scores[youtube_categories[i]] = watch_history[i] / total_watches

# Step 5: Display the results
print("YOUTUBE RECOMMENDATION SYSTEM")

# Display each category and its watch count
print("\nUSER WATCH ANALYSIS:")
for i in range(len(youtube_categories)):
    print(f"{youtube_categories[i]}: {watch_history[i]} videos watched")

# Display total watch activity
print("\nTOTAL WATCH ACTIVITY:")
print(f"Total videos watched: {total_watches}")

# Display the user's most watched category
print("\nUSER'S MOST WATCHED CATEGORY:")
print(f"Top Category: {preferred_category} ({watch_history[top_index]} watches)")

# Display preference scores
print("\nPREFERENCE SCORES:")
for category, score in scores.items():
    print(f"{category}: {score:.4f} ({score*100:.2f}%)")

# Recommendation logic
print("\nRECOMMENDATIONS:")
for i in range(len(youtube_categories)):
    if youtube_categories[i] == preferred_category:
        print(f"{youtube_categories[i]} -> HIGH PRIORITY (Recommend more of this type)")
    else:
        print(f"{youtube_categories[i]} -> LOW PRIORITY")

 