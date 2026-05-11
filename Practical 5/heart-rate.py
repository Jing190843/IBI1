# Import necessary libraries for visualization and calculations
import matplotlib.pyplot as plt
import numpy as np

# List of heart rate values for each patient
heart_rate = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# Calculate total number of patients
total_patients = len(heart_rate)

# Calculate average heart rate
avg_heart_rate = sum(heart_rate) / total_patients

# Initialize counters for each heart rate category
low = 0
medium = 0
high = 0

# Classify each heart rate into categories
for rate in heart_rate:
    if rate < 60:
        low += 1
    elif 60 <= rate <= 120:
        medium += 1
    else:
        high += 1

# Store category counts and names
category_counts = [low, medium, high]
category_names = ['Low (<60 bpm)', 'Medium (60-120 bpm)', 'High (>120 bpm)']

# Find the most frequent category
max_count = max(category_counts)
most_frequent = category_names[category_counts.index(max_count)]

# Print all results in English
print("===== Heart Rate Analysis Report =====")
print(f"Total Number of Patients: {total_patients}")
print(f"Average Heart Rate: {avg_heart_rate:.2f} bpm")
print(f"Low Heart Rate (<60 bpm): {low} patients")
print(f"Medium Heart Rate (60-120 bpm): {medium} patients")
print(f"High Heart Rate (>120 bpm): {high} patients")
print(f"\nMost Frequent Category: {most_frequent}")
print("======================================")

# Create and display pie chart
plt.pie(category_counts, labels=category_names, autopct='%1.1f%%', startangle=140)
plt.title('Heart Rate Distribution Among Patients')
plt.axis('equal')  # Ensures pie chart is a circle
plt.show()
