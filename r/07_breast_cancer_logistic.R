# Breast Cancer Prediction using Logistic Regression
# Illustrative synthetic dataset - classroom example, not a diagnostic tool.
data <- data.frame(Radius = c(9, 11, 13, 15, 17, 19, 21, 23, 14, 18, 20, 12),
                   Texture = c(11, 14, 17, 16, 21, 20, 25, 27, 18, 19, 22, 15),
                   Diagnosis = c(0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0))
print(data)

model <- glm(Diagnosis ~ Radius + Texture, data = data, family = binomial)

new_patient <- data.frame(Radius = 17, Texture = 20)
probability <- predict(model, newdata = new_patient, type = "response")

cat("\nPredicted probability:", round(probability, 3), "\n")
if (probability >= 0.5) {
  cat("Prediction: Malignant\n")
} else {
  cat("Prediction: Benign\n")
}
cat("\nResult: Logistic Regression prediction completed.\n")
