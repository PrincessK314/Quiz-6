from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def getArea(self) -> float:
        return 2 * self.radius * math.pi

class Square(Shape):
    def __init__(self, length: float) -> None:
        self.length = length
    
    def getArea(self) -> float:
        return pow(self.length, 2)

class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width
    
    def getArea(self) -> float:
        return self.length * self.width

def main():
    c = Circle(2)
    r = Rectangle(2, 4)
    s = Square(3)

    print("Circle: " + str(c.getArea()))
    print("Square: " + str(s.getArea()))
    print("Rectangle: " + str(r.getArea()))

main()