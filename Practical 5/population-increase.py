import matplotlib.pyplot as plt
import numpy as np
population_2020={'UK':66.7,'US':331.6,'CN':1426,'BRZ':208.6,'Italy':59.4}
population_2024={'UK':69.2,'US':340.1,'CN':1410,'BRZ':212.0,'Italy':58.9}
countries=list(population_2020.keys())
pop_2020=np.array(list(population_2020.values()))
pop_2024=np.array(list(population_2024.values()))
population_change_percentage=np.round(((pop_2024 - pop_2020) / pop_2020) * 100,2).tolist()
dic=dict(zip(countries,population_change_percentage))
print("各国人口增长率：", dic)
sorted_dict=dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
print("按降序排列：", sorted_dict)
print("增长率最高的国家：", max(dic, key=dic.get), "增长率：", max(dic.values()), "%")
print("增长率最低的国家：", min(dic, key=dic.get), "增长率：", min(dic.values()), "%")
plt.bar(countries, population_change_percentage, color=['blue', 'orange', 'green', 'red', 'purple'])
plt.xlabel('country')
plt.ylabel('population change rate (%)')
plt.title('2020-2024年各国人口增长率')
plt.ylim(min(population_change_percentage)*1.1, max(population_change_percentage)*1.1)
plt.show()  


                 