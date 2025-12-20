# -*- coding: utf-8 -*-

class Vector:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __repr__(self):
        return f"Vector(x={self.__x}, y={self.__y})"
    
# Exempel på användning:

if __name__ == "__main__":

    v = Vector(3, 4)
    print(v)        # Anropar __str__
    print(repr(v))      # Anropar __repr__

    v2 = eval(repr(v))  # Skapar ett nytt objekt från strängen som returneras av __repr__
    print(v2)           # Visar det nya objektet
