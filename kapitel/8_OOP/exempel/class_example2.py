# -*- coding: iso-8859-15 -*-

from class_example1 import *
from math import *

class Circle(Point):
    def __init__(self, x, y, radius):
        Point.__init__(self, x, y)
        self._radius = radius
        
    def show(self):
        x, y = self.getPosition()
        print "x =", self._x, ", y =", self._y, ", radius =", self._radius
        
    def setRadius(self, radius):
        self._radius = radius
        
    def getRadius(self):
        return self._radius
    
    def getArea(self):
        return pi*self._radius**2
    
if __name__ == "__main__":
    
    c1 = Circle(0.0, 0.0, 1.0)
    c1.setPosition(1.0, 2.0)
    c1.show()
    print "area =", c1.getArea()

