# Abstract method 
from abc import ABC, abstractmethod

class Shape(ABC):   # Cannot instantiate Shape
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)



r = Rectangle(10, 5)
print(f"Area: {r.area()}")  
print(f"Perimeter: {r.perimeter()}")  

