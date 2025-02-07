# Encapsulation - Bank Account
# A bank account should keep the balance private.
# Only deposit and withdraw methods should modify the balance.
# How would you prevent direct access to the balance?

class bank():
    def __init__(self, balance):
        self.__balance = balance

    def deposite(self, depositA):
       
        self.__balance+=depositA
        print(self.__balance)

    def withdraw(self, withdrawA):
        remain = self.__balance - withdrawA
        print(remain)

c1 = bank(23000)
c1.deposite(500) 
c1.withdraw(20000)