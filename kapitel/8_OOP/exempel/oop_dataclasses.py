# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0

    def distance_to(self, other: 'Point') -> float:
        if not isinstance(other, Point):
            raise TypeError("Argument must be a Point instance")
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
@dataclass
class Circle(Point):
    radius: float = 1.0

    def __post_init__(self):
        if not isinstance(self.radius, (int, float)) or self.radius <= 0:
            raise ValueError("Radien måste vara ett positivt tal")
        


# example usage

if __name__ == "__main__":

    p1 = Point(3, 4)
    p2 = Point(6, 8)
    p3 = Point()
    p3.x = 10
    p3.y = 10

    print(f"Avståndet mellan {p1} och {p2} är {p1.distance_to(p2)}")

    c = Circle(0, 0, 5)
    print(f"Cirkel med centrum i ({c.x}, {c.y}) och radie {c.radius}")

