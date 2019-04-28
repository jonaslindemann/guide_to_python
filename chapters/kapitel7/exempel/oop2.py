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

    def x(self):
        return self._x

    def y(self):
        return self._y



p = Point(1.0, 2.0)
print(p.x, p.y)

p.set(2.0, 3.0)
p.set_x(42.0)
p.set_y(84.0)

print(p.x())
print(p.y())