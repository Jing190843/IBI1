import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Load CSV Data
dalys_data = pd.read_csv("/Users/jing/Desktop/IBI_Practical/Practical_10/dalys-rate-from-all-causes.csv")

print("=== Dataset loaded successfully ===")

# Show first 10 rows of Year and DALYs, comment Afghanistan's highest year
print("\n=== First 10 rows (Year and DALYs) ===")
first_10_rows = dalys_data.iloc[0:10, [2, 3]]  # Columns: Year (index 2), DALYs (index 3)
print(first_10_rows)

#  Afghanistan's highest DALY value is in year 1998
afghanistan_first10 = dalys_data.loc[dalys_data['Entity'] == 'Afghanistan'].head(10)
max_daly_row = afghanistan_first10.loc[afghanistan_first10['DALYs'].idxmax()]
print(f"\n=== Afghanistan's highest DALY in first 10 years: Year {max_daly_row['Year']}, DALY = {max_daly_row['DALYs']} ===")


# Zimbabwe data, from 1990 to 2019
print("\n=== Zimbabwe DALY data (all years) ===")
zimbabwe_data = dalys_data.loc[dalys_data['Entity'] == 'Zimbabwe']
print(zimbabwe_data[['Year', 'DALYs']])

start_year = zimbabwe_data['Year'].min()
end_year = zimbabwe_data['Year'].max()
print(f"\n=== Zimbabwe data range: from {start_year} to {end_year} ===")


# Find countries with max/min DALYs in 2019, which are Lesotho and Singapore respectively
print("\n=== 2019 DALY data ===")
data_2019 = dalys_data.loc[dalys_data['Year'] == 2019, ['Entity', 'DALYs']]

max_daly_2019 = data_2019.loc[data_2019['DALYs'].idxmax()]
min_daly_2019 = data_2019.loc[data_2019['DALYs'].idxmin()]

print(f"Highest DALY in 2019: {max_daly_2019['Entity']} ({max_daly_2019['DALYs']})")
print(f"Lowest DALY in 2019: {min_daly_2019['Entity']} ({min_daly_2019['DALYs']})")

# Plot UK DALYs over time
uk_data = dalys_data.loc[dalys_data['Entity'] == 'United Kingdom']

plt.figure(figsize=(10, 5))
plt.plot(uk_data['Year'], uk_data['DALYs'], 'b-', marker='o', markersize=4, label='United Kingdom')
plt.xlabel("Year")
plt.ylabel("DALYs Rate")
plt.title("DALYs Rate Over Time - United Kingdom")
plt.xticks(rotation=-90)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("/Users/jing/Desktop/IBI_Practical/Practical_10/uk_dalys.png", dpi=150)
plt.show()

# Analyze China vs UK DALY gap over time
china_data = dalys_data.loc[dalys_data['Entity'] == 'China']

# Merge data on Year to calculate the gap
china_uk_merged = pd.merge(china_data[['Year', 'DALYs']], uk_data[['Year', 'DALYs']],
                           on='Year', suffixes=('_China', '_UK'))
china_uk_merged['Gap'] = china_uk_merged['DALYs_China'] - china_uk_merged['DALYs_UK']

print("\n=== China vs UK DALY Gap Over Time ===")
print(china_uk_merged[['Year', 'DALYs_China', 'DALYs_UK', 'Gap']])

# Plot the gap
plt.figure(figsize=(10, 5))
plt.plot(china_uk_merged['Year'], china_uk_merged['Gap'], 'r-', marker='s', markersize=4, label='China-UK DALY Gap')
plt.axhline(y=0, color='gray', linestyle='--')
plt.xlabel("Year")
plt.ylabel("DALY Gap (China - UK)")
plt.title("Changing Gap in DALYs Between China and the UK")
plt.xticks(rotation=-90)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("/Users/jing/Desktop/IBI_Practical/Practical_10/china_uk_gap.png", dpi=150)
plt.show()
