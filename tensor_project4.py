import tensorflow as tf
import numpy as np

#student Features
#maths,eng,science,aptitude test
x=np.array([
    #computer science
    [95,60,92,90],
    [90,55,88,87],
    [92,58,90,91],
    [94,62,91,89],
    [89,59,86,88],

    #business
    [60,95,65,72],
    [58,90,60,70],
    [65,92,63,75],
    [62,88,66,71],
    [59,94,61,73],

    #engineering
    [90,55,95,85],
    [88,50,92,82],
    [93,58,99,70],
    [91,54,96,86],
    [89,56,93,84],

    #education
    [70,82,72,90],
    [68,55,67,95],
    [71,45,67,89],
    [69,68,77,96],
    [71,66,89,97]

        
])

#degree programs
#0=computer science
#1=business
#2=engineering
#3=education
y=np.array([
    0,0,0,0,0,
    1,1,1,1,1,
    2,2,2,2,2,
    3,3,3,3,3

])

#build neural network
model=tf.keras.Sequential([
    #first hidden layer
    tf.keras.layers.Dense(16, activation="relu"),
    #2nd hidden layer
    tf.keras.layers.Dense(8,activation="relu"),
    #output layer
    #softmax-calculates the probability for every class
    #4 rep degree programs
    tf.keras.layers.Dense(4,activation="softmax")
])

#compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

#train the model
model.fit(x,y,epochs=50)

#making predictions
new_student=np.array([
    [92,58,90,89]
])
prediction=model.predict(new_student)
print("prediction probabilities")
print(prediction)

#find the prediction class
predicted_class=np.argmax(prediction)

degrees=[
    "computer science",
    "business",
    "engineering",
    "education"
]
print("Recommended degree:", degrees[predicted_class])