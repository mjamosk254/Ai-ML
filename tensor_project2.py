import tensorflow as tf
import numpy as np

#creating training data
x=np.array([
    [1,45],
    [2,55],
    [3,60],
    [4,68],
    [5,72],
    [6,80],
    [7,90],
])

#0 means reject
#1 means hire

y=np.array([
    0,
    0,
    0,
    1,
    1,
    1,
    1
])

#building the neural network
model=tf.keras.Sequential([
    #1st hidden layer
    tf.keras.layers.Dense(8,activation="relu"),
    #2nd hidden layer
    tf.keras.layers.Dense(4,activation="relu"),
    #ouput layer
    tf.keras.layers.Dense(1,activation="sigmoid")
])

#compiling the model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

#training the model
model.fit(x,y,epochs=50)

#make prediction
prediction=model.predict(np.array([[5,78]]))

print(prediction)