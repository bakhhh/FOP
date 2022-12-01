#
#  Practical Test 3 
#
#  accounts.py - class for bank accounts
#  
#  Student Name   : Sohailharoon Bakhshi
#  Student Number : 20605126
#  Date/prac time : 3/5/2021
#
class BankAccount ():
    interest_rate = 0.3
    def __init__(self, acc_name, acc_number, acc_balance):
        self.name = acc_name
        self.num = acc_number
        self.bal = acc_balance

    def withdraw(self, amount):
        self.bal = self.bal - amount

    def deposit(self, amount):
        self.bal = self.bal + amount

    def add_interest(self):
        self.bal += self.bal * self.interest_rate

def balances(acc):
    print('\n#### Balances of All Accounts####\n')
    total = 0
    for i in range(len(acc)):
        print("Name: ", acc[i].name, "\tNumber: ", acc[i].num, 
              "\tBalance: ", acc[i].bal)
        total = total + acc[i].bal
    print("\t\t\t\t\tTotal: ", total)
