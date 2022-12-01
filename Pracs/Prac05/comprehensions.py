#
# comprehensions.py
#

#

def triple(num):
    return num*3

numbers = []
for i in range(1,6):
    numbers.append(i)

print("Loop: ", numbers)

numbers = [i for i in range(1,6) ]
print("comprehensions: ", numbers)

tripled = []
for n in numbers:
    tripled.append(triple(n))

print("Loop: ", tripled)

tripled = [triple(n) for n in numbers]
print("comprehensions: ", tripled)

instring = input("Enter a string: ")

numstring = []

for c in instring:
    if c.isdigit():
        numstring.append(c)
print("Loop: ", numstring)

numstring = [c for c in instring if c.isdigit()]

print("comprehension: ", numstring)

words = input("Enter some words: ")

capitalised = []
for w in words.split():
    capitalised.append(w[0].upper() + w[1:])

print("Loop: ", capitalised)

capitalised = [w[0].upper()+w[1:] for w in words.split()]

print("comprehension: ", capitalised)

