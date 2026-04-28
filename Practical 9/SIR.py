import numpy as np
import matplotlib.pyplot as plt
#apply SIR model to simulate the spread of a disease in a population
#S: number of susceptible individuals
#I: number of infected individuals
#R: number of recovered individuals
total = 10000
S=[9999]
I=[1]
R=[0]

#in 1000 days
for i in range(1000):
    #calculate the number of new infections and recoveries based on the current number of infected individuals
    new_infected=0
    infect_possibility=I[-1]*0.3/10000
    infect_true=np.random.choice(range(2), S[-1], p=[1-infect_possibility, infect_possibility])
    new_infected=np.sum(infect_true==1)

    #calculate the number of new recoveries based on the current number of infected individuals
    new_recovered=0
    recover_posibility=0.05
    recover_true=np.random.choice(range(2), I[-1], p=[1-recover_posibility, recover_posibility])
    new_recovered=np.sum(recover_true==1)

    #adding the new infections and recoveries to the current number of susceptible, infected, and recovered individuals   
    delta=new_infected-new_recovered
    S.append(S[-1]-new_infected)
    I.append(I[-1]+delta)
    R.append(R[-1]+new_recovered)

#draw the figure of the SIR model simulation
S = np.array(S)
I = np.array(I)
R = np.array(R)

plt.figure(figsize=(6, 4), dpi=300)
plt.plot(S, label='S')
plt.plot(I, label='I')
plt.plot(R, label='R')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model Simulation')
plt.legend()
plt.savefig("/Users/jing/Desktop/IBI_Practical/Practical 9/SIR_simulation.png", dpi=300)          
plt.show()


    

