#
# growtharray.py - simulation of unconstrained growth
#
import matplotlib.pyplot as plt
import numpy as np

print("\nSTIMULATION - Uncontrained Growth\n")

length = 100
population = 100
growth_rate = 0.1
time_step = 0.5
num_iter = int(length / time_step)
growth_step = growth_rate * time_step

print("INITIAL VALUES:\n")
print("Simulation Length (hours): ", length)
print("Initial Population: ", population)
print("Growth Rate (per hour): ", growth_rate)
print("Time Step (part hour per step): ", time_step)
print("Num iterations (sim length * time step per hour): ",
        num_iter)
print("Growth step (growth rate per time step): ",
growth_step)

print("\nRESULTS:\n")
print("Time: ", 0, " \tGrowth: ", 0, " \tPopulation: ",100)

timearray = np.zeros(num_iter+1)
poparray= np.zeros(num_iter+1)

timearray[0] = 0
poparray[0]= population

for i in range(1, num_iter + 1 ):
    growth = growth_step * population 
    population = population + growth
    time = i * time_step
    timearray[i] = time
    poparray[i] = population
    print("Time: ", time, " \tGrowth: ", growth,
          " \tPopulation: ", population)

print("\nPROCESSING COMPLETE. \n")

plt.title('Prac 3.1: Unconstrained Growth')
plt.plot(timearray, poparray, 'r')

plt.show()

print(len(poparray))


