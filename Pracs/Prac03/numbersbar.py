#
# numbersbar.py: Read ten numbers give sum, min, max & mean
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
plt.bar([0,1,2,3,4,5,6,7,8,9],numarray, 0.9, color = 'r')
plt.savefig('numbersbar.png')
plt.show()
