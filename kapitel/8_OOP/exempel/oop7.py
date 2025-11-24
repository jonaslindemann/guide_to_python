# -*- coding: utf-8 -*-

import random

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

    x = property(get_x, set_x)
    y = property(get_y, set_y)

p0 = Point()
p1 = Point()

p0.move(10.0, 20.0)
p0.move(-5.0, -5.0)

print(p0.x, p0.y)

p1.copy_from(p0)
print(p1.x, p0.y)

