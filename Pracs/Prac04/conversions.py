# 
# conversions.py – module with functions to convert between units 
# 
# fahr2cel : Convert from Fahrenheit to Celsius. 
# 

def fahr2cel(fahr):
    """Convert from Fahrenheit to Celsius. Argument: fahr – the temperature in Fahrenheit """
    celsius = (fahr - 32) * (5/9) 
    return celsius

def fahr2kel(fahr):
    """Convert from Fahrenheit to kelvin. Argument: fahr – the temperature in Fahrenheit """
    kelvin = (fahr - 32) * (5/9) + 273.15
    return kelvin

def cel2kel(cel):
    """Convert from Celsius to kelvin. Argument: cel – the temperature in celsius """
    kelvin = (cel) - -273.15 
    return kelvin

def kel2cel(kel):
    """Convert from kelvin to Celsius. Argument: kel – the temperature in kelvin """
    celsius = (kel) - 273.15 
    return celsius

def cel2fahr(cel):
    """Convert from Celsius to Fahrenheit. Argument: cel – the temperature in celsius """
    fahr = (cel * 9/5) + 32
    return fahr

def kel2fahr(kel):
    """Convert from Kelvin to Fahrenheit. Argument: kel – the temperature in Fahrenheit """
    fahr = ((kel - 273.15) * 9/5) + 32
    return fahr
