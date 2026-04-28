import os
os.environ['PYTHONHASHSEED'] = '0' 
import numpy as np
np.random.seed() 
import matplotlib.pyplot as plt
#apply SIR model to simulate the spread of a disease in a population
#S: number of susceptible individuals
#I: number of infected individuals
#R: number of recovered individuals
#V: number of vaccinated individuals
total = 10000
total_I_curves=[]
for v in range(0,10):
    S=[9999-1000*v]
    I=[1]
    R=[0]
    for i in range(200):
        new_infected=0
        infect_possibility=I[-1]*0.3/10000
        infect_true=np.random.choice(range(2), S[-1], p=[1-infect_possibility, infect_possibility])
        new_infected=np.sum(infect_true==1)

        new_recovered=0
        recover_posibility=0.05
        recover_true=np.random.choice(range(2), I[-1], p=[1-recover_posibility, recover_posibility])
        new_recovered=np.sum(recover_true==1)

        delta=new_infected-new_recovered
        I.append(I[-1]+delta)
        S.append(S[-1]-new_infected)
        R.append(R[-1]+new_recovered)
    total_I_curves.append(I)

for idx, curve in enumerate(total_I_curves):
    plt.plot(curve, label=f"Group {idx}")

plt.xlabel('Time')
plt.ylabel('Infected Individuals (I)')
plt.title('SIR Model - Infected Population Curves')
plt.legend()
plt.show()
plt.close()

    

