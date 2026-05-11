# Initial parameters
x = 5          # Initial number of patients
y = 0.4        # Daily infection growth rate
i = 1          # Day counter
target = 91    # Target total patients

print("===== Daily Number of Infected Patients =====")
print(f"Day {i}: Initial patients = {x}")

# Loop until reaching the target number of patients
while x < target:
    i += 1
    # New infected patients on current day
    z = x * y
    next_total = x + z

    # Adjust for the last day if exceeding target
    if next_total > target:
        z = target - x

    # Print daily patient number
    print(f"Day {i}: There are {z:.2f} new patients")
    # Update total patients
    x += z

# Final summary
print("\n===== Simulation Summary =====")
print(f"Total days to reach {target} patients: {i} days")
