import tensorflow as tf
import numpy as np

#training data(input)
study_hours=np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
],dtype=float)

#correct answers(output)
exam_scores=np.array([40,50,60,70,80,90])

#create the Neural network
student_model=tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),#This tells tensor what the input data looks likes
    tf.keras.layers.Dense(1)
])

#compile the model - prepare thhe model for training
#sgd - Stochastic Gradient Descent
student_model.compile(
    optimizer="sgd",
    loss="mean_squared_error"
)  

#training the model
student_model.fit(study_hours,exam_scores,epochs=200)

#make a prediction
prediction=student_model.predict(np.array([[7.0]]))

print(prediction)