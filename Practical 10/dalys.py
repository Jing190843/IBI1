import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/jing/Desktop")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head(5))
dalys_data.info()
dalys_data.describe()
dalys_data.iloc[0:10,2:4]
my_columns=[True,True,False,True]
dalys_data.iloc[0:3,my_columns]
dalys_data.iloc[0:3,my_columns]
dalys_data.loc[2:4,"Year"]
dalys_data.loc[dalys_data.Entity=="Zimbabwe","Year"]
recent_data=dalys_data.loc[dalys_data.Year==2019,["Entity","DALYs"]]
uk=dalys_data.loc[dalys_data.Entity=="United Kingdom"]
plt.plot(uk.Year,uk.DALYs,'b+')
plt.xticks(uk.Year, rotation=-90)
plt.show()