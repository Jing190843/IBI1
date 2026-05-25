# Get user inputs
age = float(input("Please enter your age: "))
weight = float(input("Please enter your weight in kg: "))
creatinine = float(input("Please enter your serum creatinine in mg/dL: "))
gender = input("Please enter your gender (male or female): ").lower()

# Function to calculate Creatinine Clearance (Cockcroft-Gault Equation)
def calculate_creatinine_clearance(age, weight, creatinine, gender):
    # Input validation
    if not 0 <= age <= 100:
        return "Error: Please enter a valid age between 0 and 100."
    if not 20 <= weight <= 80:
        return "Error: Please enter a valid weight between 20 and 80 kg."
    if not 0 <= creatinine <= 100:
        return "Error: Please enter a valid serum creatinine between 0 and 100 mg/dL."
    if gender not in ["male", "female"]:
        return "Error: Please enter a valid gender: male or female."
    
    # Calculate using Cockcroft-Gault formula
    if gender == "male":
        clearance = ((140 - age) * weight) / (72 * creatinine)
    else:
        clearance = ((140 - age) * weight) / (72 * creatinine) * 0.85
    
    return round(clearance, 2)  # Round to 2 decimal places

# Calculate and display result
result = calculate_creatinine_clearance(age, weight, creatinine, gender)
print("\nYour Creatinine Clearance is:", result, "mL/min")