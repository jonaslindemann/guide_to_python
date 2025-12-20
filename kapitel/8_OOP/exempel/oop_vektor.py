# -*- coding: utf-8 -*-

import random, math

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

    @property
    def magnitude(self):
        return math.sqrt(self.__x**2 + self.__y**2)

    def normalize(self):
        mag = self.magnitude
        if mag > 0:
            self._x /= mag
            self._y /= mag

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.__x + other.x, self.__y + other.y)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.__x - other.x, self.__y - other.y)
    
    def __mul__(self, other: 'Vector | int | float') -> 'Vector | float':
        if isinstance(other, Vector):
            # Dot product
            return self.__x * other.x + self.__y * other.y
        else:
            # Scalar multiplication
            return Vector(self.__x * other, self.__y * other)
    
    def __xor__(self, other: 'Vector') -> float:
        """Cross product for 2D vectors (returns scalar z-component)"""
        return self.__x * other.y - self.__y * other.x
    
    def __truediv__(self, scalar: float) -> 'Vector':
        return Vector(self.__x / scalar, self.__y / scalar)
    
    def __neg__(self) -> 'Vector':
        return Vector(-self.__x, -self.__y)
    
    def __eq__(self, value: 'Vector') -> bool:
        return self.__x == value.x and self.__y == value.y

    def __str__(self) -> str:
        return "Vector(" + str(self.__x) + ", " + str(self.__y) + ")"


if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print("v1:", v1)
    print("v2:", v2)
    print("v1 + v2:", v1 + v2)
    print("v1 - v2:", v1 - v2)
    print("v1 * 2:", v1 * 2)
    print("v1 * v2:", v1 ^ v2)
    print("v1 / 2:", v1 / 2)
    print("-v1:", -v1)
    #print("v1 magnitude:", v1.magnitude)
    print("v1 == v2:", v1 == v2)
    #print("v1 . v2:", v1 * v2)
