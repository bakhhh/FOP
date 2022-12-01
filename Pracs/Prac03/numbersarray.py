#
# numbersarray.py: Read ten numbers give sum, min, max & mean
#
import numpy as np
import matplotlib.pyplot as plt
numarray = np.zeros(10)      # create an empty 10 element array

print('Enter ten numbers...')

for i in range(len(numarray)):
    print('Enter a number (', i, ')...')   
    numarray[i] = int(input())

print('Total is ', numarray.sum())
print('Minimum = ', numarray.min())
print('Maximum = ', numarray.max())
print('Mean = ', numarray.mean())


plt.title(" Numbers ")
plt.plot(numarray, 'g^')
plt.show()
