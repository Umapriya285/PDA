# Decision Tree Classification - pass/fail from study hours and attendance
import numpy as np
from sklearn.tree import DecisionTreeClassifier

X = np.array([[1, 35], [2, 42], [3, 55], [4, 58], [5, 72], [6, 65], [7, 85], [8, 92]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

prediction = model.predict([[5, 75]])
print("Study Hours: 5")
print("Attendance: 75%")
if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")
