# Simple Linear Regression - predict student marks from study hours
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[2], [3], [4], [5], [6], [7]])
y = np.array([35, 41, 52, 58, 67, 73])

model = LinearRegression()
model.fit(X, y)

predicted_marks = model.predict([[8]])
print("Predicted marks for 8 study hours:", round(predicted_marks[0], 2))

plt.scatter(X, y, color="blue", label="Actual marks")
plt.plot(X, model.predict(X), color="red", label="Regression line")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.legend()
plt.savefig("slr.png", dpi=110, bbox_inches="tight")
plt.show()
