#
# converter2.py - convert multiple values using one conversion 
#                 screen output supressed for redirection     
#
from conversions import *

def getchoice():
    print('Enter conversion type: \n',
               '   1 : Celsius to Fahrenheit\n',
               '   2 : Kelvin to Fahrenheit\n',
               '   3 : Celsius to Kelvin\n',
               '   4 : Fahrenheit to Celsius\n',
               '   5 : Fahrenheit to Kelvin\n',
               '   6 : Kelvin to Celsius\n',
               '   0 : Exit...') 
    mychoice = input()
    return mychoice

#print('\nTEMPERATURE CONVERTER\n')

#choice = getchoice()
choice = input()

#value = input('Enter value to convert (empty value to exit)...')
value = input()

while value != '':
    fvalue = float(value)
    if choice[0] == '1':
        #print('Result is : ', cel2fahr(fvalue), '\n')
        print(cel2fahr(fvalue))
    elif choice[0] == '2':
        #print('Result is : ', kel2fahr(fvalue), '\n')
        print(kel2fahr(fvalue))
    elif choice[0] == '3':
        #print('Result is : ', cel2kel(fvalue), '\n')
        print(cel2kel(fvalue))
    elif choice[0] == '4':
        #print('Result is : ', fahr2cel(fvalue), '\n')
        print(fahr2cel(fvalue))
    elif choice[0] == '5':
        #print('Result is : ', fahr2kel(fvalue), '\n')
        print(fahr2kel(fvalue))
    elif choice[0] == '6':
        #print('Result is : ', kel2cel(fvalue), '\n')
        print(kel2cel(fvalue))
    else:
        print('Invalid selection.\n')
    #value = input('Enter value to convert (empty value to exit)...')
    value = input()

#print('\nGOODBYE!\n')

