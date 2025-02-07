# Polymorphism - Payment System
# Different payment methods (Credit Card, PayPal, UPI) process payments differently.
# The method process_payment() should behave differently for each payment type.
# How would you ensure all payment classes have the process_payment() method?

# Base class
class Payment:
    def process_payment(self, amount):
        print(f"Processing payment of ₹{amount}")

class CreditCard(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class PayPal(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using PayPal")

class UPI(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using UPI")


u = Payment()
u.process_payment(2000)

