import numpy as np
import matplotlib.pyplot as plt
#the parameters of the model(size of the population, infection rate, recovery rate, and number of time steps) 
population = np.zeros((100, 100))
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
beta = 0.3    
gamma = 0.05    
time_steps = 100

#the process of the simulation
for t in range(time_steps+1):
    #copy the population
    new_pop = population.copy()
    #find the infected individuals
    infected_i, infected_j = np.where(population == 1)
    #the infection process
    for i, j in zip(infected_i, infected_j):
        neighbors = [
            (i-1, j-1), (i-1, j  ), (i-1, j+1),
            (i,   j-1), (i  , j+1), (i+1, j-1), 
            (i+1, j  ), (i+1, j+1)
        ]
        
        for ni, nj in neighbors:
            #make sure the neighbor is within the bounds of the population grid
            if 0 <= ni < 100 and 0 <= nj < 100:
                if population[ni, nj] == 0:
                    if np.random.rand() < beta:
                        new_pop[ni, nj] = 1  
    #find the infected individuals                    
    recovered_i, recovered_j = np.where(population == 1)
    #the recovery process
    for i, j in zip(recovered_i, recovered_j):
        if np.random.rand() < gamma:
            new_pop[i, j] = 2
    population = new_pop
    #draw the picture of the population every 10 time steps
    if t % 10 == 0:
        plt.figure(figsize=(6,4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time step {t}')
        plt.axis('off')
        plt.show()
