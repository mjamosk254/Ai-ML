from sklearn.tree import DecisionTreeClassifier

#step 1 training data
x=[[30],[40],[50],[60],[80],[100]]
y=["fail","fail","pass","pass","pass","pass"]
#step 2 creating the model
model=DecisionTreeClassifier()
#step 3 training the model
model.fit(x,y)
#step 4 making the predictions
print(model.predict([[75]]))
print(model.predict([[25]]))


movie_ratings=[[1],[2],[3],[4],[5]]
customer_opinion=["dislike","dislike","like","like","like"]
movie_predictor=DecisionTreeClassifier()
movie_predictor.fit(movie_ratings,customer_opinion)
print(movie_predictor.predict([[6]]))
