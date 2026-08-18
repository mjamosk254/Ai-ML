#multi label classification 
import tensorflow as tf
import numpy as np

#movie features
#[action,comedy,romance,adventure]
x=np.array([
    #action & adventure
    [98,10,5,96],
    [95,12,10,95],
    [96,12,10,95],

    #comedy & romance
    [10,96,92,12],
    [12,94,95,15],
    [8,95,90,10],

    #action & comedy & adventure
    [95,90,10,95],
    [94,92,12,94],
    [96,88,8,96],

    #romance only
    [5,15,98,8],
    [8,10,96,10],
    [10,12,95,6],
])
y=np.array([
    [1,0,0,1],
    [1,0,0,1],
    [1,0,0,1],

    [0,1,1,0],
    [0,1,1,0],
    [0,1,1,0],

    [1,1,0,1],
    [1,1,0,1],
    [1,1,0,1],

    [0,0,1,0],
    [0,0,1,0],
    [0,0,1,0],
    
])

#build the neural network
model=tf.keras.Sequential([
    tf.keras.layers.Dense(16,activation="relu"),
    tf.keras.layers.Dense(8,activation="relu"),
    tf.keras.layers.Dense(4,activation="sigmoid"),
])

#compile the model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

#train the model
model.fit(x,y,epochs=50)

#make a prediction
new_movie=np.array([
    [96,100,5,79]
])

prediction=model.predict(new_movie)
print("\nprediction probabilities")
print(prediction)

#genre names
genres=[
    "action",
    "comedy",
    "romance",
    "adventure"
]

print("\npredicted genres")

for i in range(len(genres)):
    if prediction[0][i] >=0.5:
        print(genres[i])
