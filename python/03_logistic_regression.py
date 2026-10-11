# Logistic Regression - predict pass/fail from study hours
import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([0, 0, 0, 1, 0, 1, 1, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

prediction = model.predict([[5]])
print("Study Hours: 5")
if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")
