# -*- coding: utf-8 -*-

import random, math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def copy_from(self, p):
        self._x = p.x
        self._y = p.y

    def __str__(self):
        return "Point("+str(self._x)+", "+str(self._y)+")"

    def area(self):
        return 0.0

    x = property(get_x, set_x)
    y = property(get_y, set_y)

class Circle(Point):
    def __init__(self, x=0.0, y=0.0, r=1.0):
         super().__init__(x, y)
        self._r = r

    def set_r(self, r):
        self._r = r

    def get_r(self):
        return self._r

    def copy_from(self, c):
        super().copy_from(c)
        self.r = c.r

    def area(self):
        return math.pi*math.pow(self._r, 2)

    def __str__(self):
        return "Circle("+str(self.x)+", "+str(self.y)+", "+str(self._r)+")"

    r = property(get_r, set_r)

p = Point(1.0, 2.0)
c = Circle(2.0, 4.0, 8.0)

c.r = 10.0

p.move(1.0, 1.0)
c.move(1.0, 1.0)

print(p)
print(c)
print(c.area())
