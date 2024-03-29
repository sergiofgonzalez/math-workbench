from my_vectors import to_cartesian, add, rotate2d
from math import pi, sqrt, sin, cos
from random import randint, uniform
from my_linear_equations import do_segments_intersect

class PolygonModel():
    def __init__(self, points):
        self.points = points
        self.rotation_angle = 0
        # x, y keeps track of the center of the polygon
        self.x = 0
        self.y = 0

        # added in section 9.1.1
        # vx, vy are the velocity components
        self.vx = 0
        self.vy = 0

    # added in section 7.1.2
    # modified to handle rotations in Exercise 1
    def transformed(self):
        # before rotation was:
        # return [add((self.x, self.y), v) for v in self.points]
        rotated_points = [rotate2d(self.rotation_angle, point) for point in self.points]
        return [add((self.x, self.y), rotated_point) for rotated_point in rotated_points]


    # added in section 9.1.2
    def move(self, milliseconds):
        dx, dy = (self.vx * milliseconds / 1000, self.vy * milliseconds / 1000)
        self.x, self.y = add((self.x, self.y), (dx, dy))

        # added in section 9.1.3 (teleportation when going offscreen)
        if self.x < -10:
            self.x += 20
        if self.y < -10:
            self.y += 20
        if self.x > 10:
            self.x -= 20
        if self.y > 10:
            self.y -= 20

    # Added in Exercise 7.14
    def segments(self):
        points_count = len(self.points)
        points = self.transformed()
        return [(points[i], points[(i + 1) % points_count]) for i in range(0, points_count)]

    # Added in Exercise 7.14
    def does_intersect(self, other_segment):
        for segment in self.segments():
            if do_segments_intersect(other_segment, segment):
                return True
        return False

    # Added in Exercise 7.14
    def does_collide(self, other_polygon):
        for other_poly_segment in other_polygon.segments():
            if self.does_intersect(other_poly_segment):
                return True
        return False

class Ship(PolygonModel):
    def __init__(self):
        super().__init__([(0.5, 0), (-0.25, 0.25), (-0.25, -0.25)])

    # added in section 7.1.3
    def laser_segment(self):
        dist = 20 * sqrt(2)
        x, y = self.transformed()[0]
        return ((x,y), (x + dist * cos(self.rotation_angle), y + dist * sin(self.rotation_angle)))

class Asteroid(PolygonModel):
    def __init__(self):
        sides = randint(5, 9)
        points = [to_cartesian((uniform(0.5, 1.0), 2 * pi * i / sides))
            for i in range(0, sides)
        ]
        super().__init__(points)

        # assign random velocity values
        self.vx = uniform(-1, 1)
        self.vy = uniform(-1, 1)

# Added in Exercise 7.2
def to_pixels_factory(x_min, x_max, y_min, y_max, width, height):
    """Maps Math model coordinates to pixels in the game window
    """
    x_size = x_max - x_min
    y_size = y_max - y_min
    def new_to_pixels_function(x, y):
        x_game = (width / x_size) * x - (x_min * width / x_size)
        y_game = -(height / y_size) * y + (y_max * height / y_size)
        return (x_game, y_game)
    return new_to_pixels_function

