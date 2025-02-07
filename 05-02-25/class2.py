# Inheritance - Vehicle & Car
# A Car is a type of Vehicle and shares common properties.
# The Car class should reuse the Vehicle class attributes.
# How can Car add extra features like fuel_type without rewriting code?

class Vehicle():

    def fuel_type(self):
        print("petrol")

class Car(Vehicle):
    def fuel_type(self):
        print("diesel")

c1 = Car()
c1.fuel_type()