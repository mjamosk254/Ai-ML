#Multi-class classification
import tensorflow as tf
import numpy as np

#Employee Features
#[ Communication, Technical, Numerical, Creativity]
x=np.array([
    [90,30,40,50],  #HR
    [45,40,95,35],  #Finance
    [35,95,50,40],  #IT
    [75,45,40,90],  #Marketing
    [88,35,45,60],  #HR
    [40,45,90,30],  #Finance
    [30,98,55,45],  #IT
    [80,40,35,95]   #Marketing
     
])

#Department labels
#0 - HR
#1 - Finance
#2 - IT
#3 - Marketing
y=np.array([
    0,
    1,
    2,
    3,
    0,
    1,
    2,
    3
])

#Build our neural network
model=tf.keras.Sequential([
    #first hidden layer
    tf.keras.layers.Dense(16, activation="relu"),
    #2nd hidden layer
    tf.keras.layers.Dense(8,activation="relu"),
    #output layer
    #softmax-calculates the probability for every class
    tf.keras.layers.Dense(4,activation="softmax")
])

#compile the model
#predict no.s (regression)-use mean_squared-error
#predict two classes(Binary classification0)-binary crossentropy
#predict 3 or more classes(multi-class classification)- sparse_categorical_crossentropy
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

#Training the model
model.fit(x,y,epochs=20)

#making predictions
new_employee=np.array([
    [40,92,55,42]
])
prediction=model.predict(new_employee)
print(prediction)