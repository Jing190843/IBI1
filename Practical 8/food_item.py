# Define food_item class with attributes for name, calories, protein, carbohydrates, and fat
class FoodItem(object):
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat

# Define a function to calculate total calories, protein, carbs, fat
def calculate_nutrition(food_list):
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0

    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbohydrates += food.carbohydrates
        total_fat += food.fat

    # Print total nutrition
    print("\n===== DAILY NUTRITION SUMMARY =====")
    print(f"Total Calories: {total_calories} kcal")
    print(f"Total Protein: {total_protein} g")
    print(f"Total Carbohydrates: {total_carbohydrates} g")
    print(f"Total Fat: {total_fat} g")

    # Warning system
    warnings = []
    if total_calories > 2500:
        warnings.append("⚠ WARNING: Calorie intake exceeds recommended daily limit.")
    if total_fat > 90:
        warnings.append("⚠ WARNING: Fat intake exceeds recommended daily limit.")

    if warnings:
        print("\n" + "\n".join(warnings))
    else:
        print("\nAll nutrition levels are within recommended limits.")

# Function to let user INPUT food list MANUALLY
def input_food_list():
    food_list = []
    print("\n===== ENTER YOUR FOOD ITEMS =====")
    print("Type 'done' when you are finished.\n")

    while True:
        name = input("Food name (or 'done'): ").strip()
        if name.lower() == "done":
            break

        # Input calories, protein, carbs, fat
        calories = float(input("Calories: "))
        protein = float(input("Protein (g): "))
        carbs = float(input("Carbohydrates (g): "))
        fat = float(input("Fat (g): "))

        # Create food object and add to list
        food = FoodItem(name, calories, protein, carbs, fat)
        food_list.append(food)
        print(" Food added!\n")

    return food_list

# Main program
if __name__ == "__main__":
    # Choose mode: manual input
    daily_food = input_food_list()

    # Calculate and show result
    if daily_food:
        calculate_nutrition(daily_food)
    else:
        print("No food items entered.")