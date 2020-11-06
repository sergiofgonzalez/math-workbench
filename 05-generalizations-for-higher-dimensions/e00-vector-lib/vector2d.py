from vector import Vector

class Vec2(Vector):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def scale(self, scalar):
        return Vec2(scalar * self.x, scalar * self.y)

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __repr__(self):
        return 'Vec2({}, {})'.format(self.x, self.y)  