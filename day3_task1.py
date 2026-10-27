import numpy as np

#create marks
marks = np.array([[70,80,90],
                 [60,75,85],
                 [88,92,79],
                 [55,65,70]])

print("Shape:",marks.shape)
print("dtype:",marks.dtype)
print("Size:",marks.size)

# slicing

first_two_students = marks[:2]
print("first_two_students:",first_two_students)

last_subject = marks[:,-1]
print("last_subject:",last_subject)

#average 

print("Student averages:",np.round(np.mean(marks,axis=1),2))
print("Subject averages:",np.mean(marks,axis=0))

grace_numbers = marks+5

weights =np.array([0.3,0.3,0.4])
weighted_scores = np.dot(marks,weights)

print("Weighted scores:",weighted_scores)

numbers = np.arange(12)
reshaped = numbers.reshape(3,4)