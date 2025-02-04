# Create a Car class with the following properties and methods:
# Attributes: brand, model, year
# Method: start_engine() that prints "The [brand] [model] engine has started."

class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"the {self.brand} {self.model} engine has started")

audi = Car("audi", 123, 2345)
BMW = Car("BMW", 12, 2024)

audi.start_engine()

