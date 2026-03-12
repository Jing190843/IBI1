age = float(input("Please enter your age: "))
weight = float(input("Please enter your weight in kg: "))
creatine = float(input("Please enter your serum creatinine in mg/dL: "))
gender= input("Please enter your gender as male or female: ")
#gain the inputs from the user, and convert them to the correct data type
def calculate_creatinine_clearance(age, weight, creatine,gender):
    if not 0<=age<=100:
        return "Please enter a valid age between 0 and 100."
    if not 20<=weight<=80:
        return "Please enter a valid weight between 20 and 80 kg."
    if not 0<=creatine<=100:
        return "Please enter a valid serum creatinine level between 0 and 100 mg/dL."
    if gender not in ["male", "female"]:
        return "Please enter a valid gender as male or female"
    #check whether the inputs are valid, if not, return an error message
    if gender == "male":
        result = ((140-age)*weight)/(72*creatine)
    else:
        result = ((140-age)*weight)/(72*creatine) * 0.85
    return result
print("Your creatine clearance is: ",calculate_creatinine_clearance(age, weight, creatine,gender),"mL/min")
#make calculations and print the result