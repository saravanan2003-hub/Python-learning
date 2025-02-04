# Create a
# BankAccount class with:
# Attributes: account_holder, balance
# Methods:
# deposit(amount) → Adds money
# withdraw(amount) → Deducts money (if balance is enough)
# check_balance() → Prints current balance
# Example Usage:
# python
# acc = BankAccount("John", 1000)
# acc.deposit(500)
# acc.withdraw(200)
# acc.check_balance()
# Expected Output:
# yaml
# Deposit Successful! New Balance: 1500
# Withdrawal Successful! New Balance: 1300
# Current Balance: 1300

class Bank():
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        newBalance = self.balance + amount
        print(f"Deposit Successful! New Balance:{newBalance}")


    def withdraw(self,amount):
        remaningMoney = self.balance - amount
        print(f"Withdrawal Successful! New Balance: {remaningMoney}")

    def check_balance(self):
        print(f"Your current balance {self.balance}")


acc = Bank("John", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.check_balance()