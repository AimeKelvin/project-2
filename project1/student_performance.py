import matplotlib.pyplot as plt
import numpy as np

# Sample students
students = ["Alice", "Ben", "Chloe"]

# Simulated monthly performance data (values between 60–100)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

np.random.seed(42)  # for repeatable results

# Random scores per student
scores = {student: np.random.randint(60, 100, size=12) for student in students}

# Plot the line chart
plt.figure(figsize=(10, 6))
for student, values in scores.items():
    plt.plot(months, values, marker='o', label=student)

plt.title("Student Performance Over the Last Year")
plt.xlabel("Month")
plt.ylabel("Performance Score")
plt.ylim(50, 100)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show the chart
plt.show()
