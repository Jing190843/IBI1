import matplotlib.pyplot as plt
import numpy as np
heart_rate=[72,60,126,85,90,59,76,131,88,121,64]
count= len(heart_rate)
avg_heart_rate= sum(heart_rate)/count
low=0
medium=0
high=0
for rate in heart_rate:
    if rate < 60:
        low += 1
    elif 60 <= rate <= 120:
        medium += 1
    else:
        high += 1
print(f"Average Heart Rate: {avg_heart_rate:.2f} bpm")
print(f"Low Heart Rate (<60 bpm): {low}")
print(f"Medium Heart Rate (60-120 bpm): {medium}")  
print(f"High Heart Rate (>120 bpm): {high}")
numbers=[low,medium,high]
categories=['Low (<60 bpm)','Medium (60-120 bpm)','High (>120 bpm)']
plt.pie(numbers, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Heart Rate Distribution')
plt.axis('equal')
plt.show()  