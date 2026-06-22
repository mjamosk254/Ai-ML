# Project 1: Scholarship Approval Predictor
# Supervised Learning using DecisionTreeClassifier

from sklearn.tree import DecisionTreeClassifier

# Step 1: Create training dataset (at least 8 students)
# Features: [Marks (out of 100), Attendance Percentage (out of 100)]
# Labels: 'Approved' or 'Rejected'

student_data = [
    [85, 92],   # Student 1
    [78, 88],   # Student 2
    [45, 60],   # Student 3
    [92, 95],   # Student 4
    [55, 70],   # Student 5
    [30, 45],   # Student 6
    [88, 90],   # Student 7
    [65, 75],   # Student 8
    [40, 50],   # Student 9
    [95, 98],   # Student 10
]

# Labels corresponding to each student
labels = [
    'Approved',   # 85 marks, 92% attendance
    'Approved',   # 78 marks, 88% attendance
    'Rejected',   # 45 marks, 60% attendance
    'Approved',   # 92 marks, 95% attendance
    'Rejected',   # 55 marks, 70% attendance
    'Rejected',   # 30 marks, 45% attendance
    'Approved',   # 88 marks, 90% attendance
    'Rejected',   # 65 marks, 75% attendance
    'Rejected',   # 40 marks, 50% attendance
    'Approved',   # 95 marks, 98% attendance
]

# Step 2: Create and train the model
model = DecisionTreeClassifier()
model.fit(student_data, labels)

# Step 3: Make predictions for at least 3 new students
new_students = [
    [90, 94],   # New Student 1
    [50, 65],   # New Student 2
    [75, 85],   # New Student 3
]

predictions = model.predict(new_students)

# Step 4: Print the predictions
print(model.predict([[90,94]]))
print(model.predict([[50,65]]))
print(model.predict([[75,85]]))