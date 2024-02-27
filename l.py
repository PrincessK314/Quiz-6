import math

class Shape():
    def getArea(self):
        raise NotImplementedError("Subclasses must implement getArea")

class ChangableWidthHeight():
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
        
    def setWidth(self, width: float) -> None:
        self.width = width
    
    def setHeight(self, height: float) -> None:
        self.height = height

#Technically, if a circle has a diffent width and height, it's an oval
class Circle(Shape, ChangableWidthHeight):
    def getArea(self) -> float:
        return (self.width * 0.5) * (self.height * 0.5) * math.pi
    
class Rectangle(Shape, ChangableWidthHeight):
    def getArea(self) -> float:
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def getArea(self) -> float:
        return self.base * self.height * 0.5

class Polygon(Shape):
    def getArea(self):
        return "polygon area"

def displayArea(s: Shape) -> None:
    print("Area: " + str(s.getArea()))

def changeDimension(s: ChangableWidthHeight, w: float, h: float) -> None:
    s.setHeight(h)
    s.setWidth(w)

def main():
    t = Triangle(2, 2)
    c = Circle(4, 4)
    r = Rectangle(3, 6)
    p = Polygon()

    displayArea(t)
    displayArea(c)
    displayArea(r)
    displayArea(p)

    changeDimension(c, 3, 2)
    #changeDimension(t, 3, 2)
    changeDimension(r, 3, 2)

    displayArea(t)
    displayArea(c)
    displayArea(r)

main()