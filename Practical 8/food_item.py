#define food_item class with attributes for name, calories, protein, carbohydrates, and fat
class food_item(object):
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
    #define a function to calculate total calories, protein, carbohydrates, and fat from a list of food items, and print a warning if the total calories or fat exceeds recommended daily limits
    def food_calculate(food_list):
        total_calories = 0
        total_protein = 0
        total_carbohydrates = 0            
        total_fat = 0
        for food in food_list:
            total_calories += food.calories
            total_protein += food.protein
            total_carbohydrates += food.carbohydrates
            total_fat += food.fat
        print(f"Total Calories: {total_calories}")
        print(f"Total Protein: {total_protein}g")
        print(f"Total Carbohydrates: {total_carbohydrates}g")
        print(f"Total Fat: {total_fat}g")

        warning= []
        if total_calories > 2500:
            warning.append("Calorie intake exceeds the recommended daily limit.")
        if total_fat > 90:
            warning.append("Fat intake exceeds the recommended daily limit.")
            
        print("\n".join(warning))

#example usage
if __name__ == "__main__":
    apple = food_item("Apple", 95, 0.5, 25, 0.3)
    banana = food_item("Banana", 105, 1.3, 27, 0.4)
    chicken_breast = food_item("Chicken Breast", 165, 31, 0, 3.6)
    daily_food = [apple, banana, chicken_breast]
    food_item.food_calculate(daily_food)
            