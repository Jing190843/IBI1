# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Population data in millions
population_2020 = {'UK': 66.7, 'US': 331.6, 'CN': 1426, 'BRZ': 208.6, 'Italy': 59.4}
population_2024 = {'UK': 69.2, 'US': 340.1, 'CN': 1410, 'BRZ': 212.0, 'Italy': 58.9}

# Get country list and population values
countries = list(population_2020.keys())
pop_2020 = np.array(list(population_2020.values()))
pop_2024 = np.array(list(population_2024.values()))

# Calculate population change percentage
population_change_percentage = np.round(((pop_2024 - pop_2020) / pop_2020) * 100, 2).tolist()

# Create dictionary for growth rates
growth_dict = dict(zip(countries, population_change_percentage))

# Print results
print("Population Growth Rate by Country: ", growth_dict)

# Sort from highest to lowest growth rate
sorted_dict = dict(sorted(growth_dict.items(), key=lambda x: x[1], reverse=True))
print("Sorted in Descending Order: ", sorted_dict)

# Find highest and lowest growth
highest_country = max(growth_dict, key=growth_dict.get)
highest_rate = max(growth_dict.values())
lowest_country = min(growth_dict, key=growth_dict.get)
lowest_rate = min(growth_dict.values())

print("Country with Highest Growth Rate: ", highest_country, " - Growth: ", highest_rate, "%")
print("Country with Lowest Growth Rate: ", lowest_country, " - Growth: ", lowest_rate, "%")

# Plot bar chart (ALL ENGLISH)
plt.bar(countries, population_change_percentage, color=['blue', 'orange', 'green', 'red', 'purple'])
plt.xlabel('Country')
plt.ylabel('Population Change Rate (%)')
plt.title('Population Growth Rate from 2020 to 2024')

# Set Y-axis range
plt.ylim(min(population_change_percentage) * 1.1, max(population_change_percentage) * 1.1)

# Show chart
plt.show()
