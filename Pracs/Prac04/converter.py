#
# converter.py - convert multiple values using various conversions
# 
from conversions import *

print('\nTEMPERATURE CONVERTER\n')

print('Enter conversion type: \n',
               '   1 : Celsius to Fahrenheit\n',
               '   2 : Kelvin to Fahrenheit\n',
               '   3 : Celsius to Kelvin\n',
               '   4 : Fahrenheit to Celsius\n',
               '   5 : Fahrenheit to Kelvin\n',
               '   6 : Kelvin to Celsius\n',
               '   0 : Exit...') 
choice = input()

while choice[0] != '0':
    value = input('Enter value to convert...')
    fvalue = float(value)
    if choice[0] == '1':
        print('Result is : ', cel2fahr(fvalue), '\n')
    elif choice[0] == '2':
        print('Result is : ', kel2fahr(fvalue), '\n')
    elif choice[0] == '3':
        print('Result is : ', cel2kel(fvalue), '\n')
    elif choice[0] == '4':
        print('Result is : ', fahr2cel(fvalue), '\n')
    elif choice[0] == '5':
        print('Result is : ', fahr2kel(fvalue), '\n')
    elif choice[0] == '6':
        print('Result is : ', kel2cel(fvalue), '\n')
    else:
        print('Invalid selection.\n')
    print('Enter conversion type: \n',
               '   1 : Celsius to Fahrenheit\n',
               '   2 : Kelvin to Fahrenheit\n',
               '   3 : Celsius to Kelvin\n',
               '   4 : Fahrenheit to Celsius\n',
               '   5 : Fahrenheit to Kelvin\n',
               '   6 : Kelvin to Celsius\n',
               '   0 : Exit...')
    choice = input()

print('\nGOODBYE!\n')

