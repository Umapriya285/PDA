# Naive Bayes Classification - pass/fail from study hours
import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([0, 0, 0, 0, 1, 0, 1, 1, 1, 1])

model = GaussianNB()
model.fit(X, y)

prediction = model.predict([[4]])
print("Study Hours: 4")
if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")
