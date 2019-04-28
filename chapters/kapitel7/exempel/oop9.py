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

class Line:
    def __init__(self):
        self._p0 = Point()
        self._p1 = Point()
        
    def get_p0(self):
        return self._p0
    
    def get_p1(self):
        return self._p1
    
    def set_p0(self, p0):
        self._p0 = p0
        
    def set_p1(self, p1):
        self._p1 = p1
        
    def length(self):
        return math.sqrt(
                math.pow(self._p1.x - self.p0.x, 2) + 
                math.pow(self._p1.y - self.p0.y, 2))
        
    def __str__(self):
        return_string = "Line from: \n\t"
        return_string += str(self._p0) + "\n"
        return_string += "To: \n\t"
        return_string += str(self._p1) + "\n"
        return_string += "Length: \n\t"
        return_string += str(self.length())+"\n"
        return return_string
        
    p0 = property(get_p0, set_p0)
    p1 = property(get_p1, set_p1)
    
line = Line()

line.p0.x = 0.0
line.p0.y = 2.0
line.p1.x = 3.0
line.p1.y = 4.0

print(line)

line.p0.move(-1.0, -1.0)

print(line)

p3 = Point(5.0, 5.0)
p4 = Point(10.0, 10.0)

line.p0 = p3
line.p1 = p4

print(line)

