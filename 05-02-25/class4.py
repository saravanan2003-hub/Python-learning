# Abstraction - Vehicle System
# Every vehicle (Car, Bike, Bus) has a start_engine() method.
# The Vehicle class should define this method but not implement it.
# How would you ensure that every subclass has its own engine-starting mechanism?

from abc import ABC, abstractmethod

class vehicle:
    @abstractmethod
    def start_engine(self):
       pass
class car(vehicle):
    def start_engine(self):
        print(f" engine has started")


c1 = car()
c1.start_engine()

