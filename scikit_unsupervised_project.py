import numpy as np
from sklearn.cluster import KMeans
#age against spending amount
data=np.array([
    [20,1000],
    [22,2500],
    [25,4000],
    [40,20000],
    [45,35000],
    [50,70000]
])
#create a model
data_model=KMeans(n_clusters=2,n_init=10)
#training the model
data_model.fit(data)
#view the results
print(data_model.labels_)
#predict new data
print(data_model.predict([[27,45000]]))
print(data_model.predict([[58,65000]]))

#student behavior grouping AI
student_data=np.array([
    [1,30],
    [2,40],
    [3,50],
    [4,60],
    [5,70],
    [6,80],
    [7,90],
    [8,100]
])
#create a model
student_model=KMeans(n_clusters=3,n_init=10)
#training the model
student_model.fit(student_data)
#view the results
print(student_model.labels_)
#predict new data
print(student_model.predict([[7,67]]))