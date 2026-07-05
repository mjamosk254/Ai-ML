import tensorflow as tf
#one dimentional tensor
numbers=tf.constant([10,20,30,40,50])
print(numbers)
print(tf.__version__)

#two dimensional tensor
student_marks=tf.constant([
    [70,80],
    [90,60]
])
print(student_marks)

#tensor operations
marks=tf.constant([70,60,80,55,77])

#sum
print(tf.reduce_sum(marks))

#Avg
print(tf.reduce_mean(tf.cast(marks,tf.float32)))

#Highest value
print(tf.reduce_max(marks))

#lowest value
print(tf.reduce_min(marks))

#index of the highest value
print(tf.argmax(marks))

#index of the lowest value
print(tf.argmin(marks))