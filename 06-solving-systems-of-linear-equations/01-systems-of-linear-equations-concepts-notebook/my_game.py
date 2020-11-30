from my_vectors import to_cartesian, add
from math import pi, sqrt, sin, cos
from random import randint, uniform        

class PolygonModel():
    def __init__(self, points):
        self.points = points
        self.rotation_angle = 0
        # x, y keeps track of the center of the polygon
        self.x = 0
        self.y = 0

    # added in section 7.1.2
    def transformed(self):
        return [add((self.x, self.y), v) for v in self.points]        

class Ship(PolygonModel):
    def __init__(self):
        super().__init__([(0.5, 0), (-0.25, 0.25), (-0.25, -0.25)])

    # added in section 7.1.3
    def laser_segment(self):
        dist = 2 * sqrt(2)
        x, y = self.transformed()[0]
        return ((x,y), (x + dist * cos(self.rotation_angle), y + dist * sin(self.rotation_angle)))

class Asteroid(PolygonModel):
    def __init__(self):
        sides = randint(5, 9)
        points = [to_cartesian((uniform(0.5, 1.0), 2 * pi * i / sides))
            for i in range(0, sides)
        ]
        super().__init__(points)