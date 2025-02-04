# Create a
# Rectangle class with:
# Attributes: length, width
# Methods:
# area() → Returns area
# perimeter() → Returns perimeter
# Example Usage:
# python
# r1 = Rectangle(10, 5)
# print(r1.area())       # Output: 50
# print(r1.perimeter())  # Output: 30

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)
    
    def perimeter(self):
        print(2*(self.length + self.width))

r1 = Rectangle(10, 5)
r1.area()       # Output: 50
r1.perimeter()  # Output: 30





