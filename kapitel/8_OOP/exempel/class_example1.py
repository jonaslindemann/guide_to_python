# -*- coding: iso-8859-15 -*-

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def show(self):
        print "x =", self._x, ", y =", self._y

    def setPosition(self, x, y):
        self._x = x
        self._y = y

    def getPosition(self):
        return self._x, self._y

if __name__ == "__main__":

    p1 = Point(0.0, 0.0)
    p1.show()
    p1.setPosition(2.0, 3.0)
    p1.show()
    
    p2 = Point(1.0, 2.0)
    p2.show()
    x, y = p2.getPosition()
    print x, y