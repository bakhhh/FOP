#
# bucket2.py - bucket list builder
# 

print('\nBUCKET LIST BUILDER\n')

bucket = []

choice = input('Enter selection: e(X)it, (A)dd, (L)ist...')
choice = choice.upper()

while choice[0] != 'X':
    if choice[0] == 'A':
        print('Enter list item...')
        newitem = input()
        bucket.append(newitem)
    elif choice[0] == 'D':
        print('The bucket List is...')
        for index in range (len(bucket)):
            print("  ", index, " - ", bucket[index])
        delitem = input("which item do you want to delete?...")
        del bucket[int(delitem)]
    elif choice[0] == 'L':
        print('The bucket list is...')
        for item in bucket:
            print(" - ", item)
    else:
        print('Invalid selection.')
    print()
    choice =  input( 'Enter selection: e(X)it, (A)dd, (D)elete, (L)ist..')
    choice = choice.upper()

print('\nGOODBYE!\n')

