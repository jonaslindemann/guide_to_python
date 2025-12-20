# -*- coding: utf-8 -*-

from calendar import c

class Point:
    def __init__(self, x=0.0, y=0.0):
        if not isinstance(x, (int, float)):
            raise ValueError("x must be a number")
        if not isinstance(y, (int, float)):
            raise ValueError("y must be a number")
        
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("x must be a number")
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("y must be a number")
        self.__y = value

    def distance_to(self, other: 'Point') -> float:
        if not isinstance(other, Point):
            raise TypeError("Argument must be a Point instance")
        return ((self.__x - other.x) ** 2 + (self.__y - other.y) ** 2) ** 0.5
    
class Circle(Point):
    def __init__(self, x=0.0, y=0.0, radius=1.0):
        super().__init__(x, y)
        self.radius = radius  # Will use the setter for validation

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Radien måste vara ett positivt tal")
        self.__radius = value

    def set_radius_safely(self, value):
        try:
            self.radius = value
        except ValueError as e:
            print(f"Fel vid tilldelning av radie: {e}")

    def area(self) -> float:
        import math
        return math.pi * self.__radius ** 2

    def circumference(self) -> float:
        import math
        return 2 * math.pi * self.__radius
    
# Example usage:
if __name__ == "__main__":

    c = Circle(0, 0, 5)

    # Hantering av fel genom undantag

    try:
        c.radius = -10
    except ValueError as e:
        print(f"Ett undantag fångades vid tilldelning av radie: {e}")

    # Säker metod för att sätta radien

    if not c.set_radius_safely(-3):
        print("Radien förblev oförändrad:", c.radius)
