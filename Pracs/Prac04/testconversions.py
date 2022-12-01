# 
# testConversions.py - tests the functions in conversions.py 
# 
from conversions import * 

print("\nTESTING CONVERSIONS\n") 

testF = 100 
testC = fahr2cel(testF) 

print("Fahrenheit is ", testF, " Celsius is ", testC) 
print()

testC = 37.7
testF = cel2kel(testC) 

print("Celsius is ", testC, " Fahrenheit is ", testF) 
print()

testC = 37.7
testK = cel2kel(testC) 

print("Celsius is ", testC, " Kelvin is ", testK) 
print()

testK = 100
testC = kel2cel(testK) 

print("Kelvin is ", testK, " Celsius is ", testC) 
print()

testF = 37.7 
testK = fahr2kel(testF) 

print("Fahrenheit is ", testF, " Kelvin is ", testK) 
print()

testK = 100
testF = kel2fahr(testK) 

print("Kelvin is ", testK, " Fahrenheit is ", testF) 
print()

print(fahr2cel.__doc__)
