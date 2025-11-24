# -*- coding: utf-8 -*-

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

    def __str__(self):
        return "Point("+str(self._x)+", "+str(self._y)+")"

    x = property(get_x, set_x)
    y = property(get_y, set_y)

p = Point()

p.x = 42.0
p.y = 84.0

print(p)
