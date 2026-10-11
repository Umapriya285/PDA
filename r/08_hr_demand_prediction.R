# HR Analytics - predict next month's employee demand
hr_data <- data.frame(Month = 1:6, Employees = c(18, 21, 23, 27, 29, 34))
cat("Historical HR Data:\n")
print(hr_data)

model <- lm(Employees ~ Month, data = hr_data)
next_month <- data.frame(Month = 7)
predicted_demand <- predict(model, newdata = next_month)

cat("\nNext Month:", next_month$Month, "\n")
cat("Predicted Employee Demand:", round(predicted_demand), "\n")
cat("\nResult: HR demand prediction completed.\n")
