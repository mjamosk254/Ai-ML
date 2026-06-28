import numpy as np
#categories of contents available on netflix
contents_types=["Action","Romance","Comedy","Investigation","Reality"]
#no. of times user watched each type
watch_history=np.array([10,3,4,7,1])

#step 1 - To find the most watched content type
#to get the index of the highest watched category
top_index=np.argmax(watch_history)
#convert the index to actual content name
preferred_content=contents_types[top_index]

#step 2 - calculate preference scores
#total watched activities across all categories
total_watches=sum(watch_history)
#a dict to  store preference strength for each category
scores={}
for i in range(len(contents_types)):
    #formula: score=watch_history[i] / total_watches
    scores[contents_types[i]]=watch_history[i]/total_watches

#step 3 - display user behavior
print("\nUSER WATCH ANALYSIS:\n")
for i in range(len(contents_types)):
    print(contents_types[i], "watched:", watch_history[i])

#step 4 - show top preference
print("\nUSER TOP PREFERENCE:")
print(preferred_content)

#step 5 - recomendation logic
print("\nRECOMENDATIONS\n")
for i in range(len(contents_types)):
    if contents_types[i]==preferred_content:
        print(contents_types[i], "-> HIGH PRIORITY (recomend more of this type)")
    else:
        print(contents_types[i], "-> LOW PRIORITY")    
        