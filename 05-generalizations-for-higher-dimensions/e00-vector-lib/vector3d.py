from vector import Vector

class Vec3(Vector):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.coordinates = (x, y, z) # compatibility with CoordinateVector

    @classmethod
    def zero(cls):
        return Vec3(0, 0, 0)

    def add(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def scale(self, scalar):
        return Vec3(scalar * self.x, scalar * self.y, scalar * self.z)

    def __eq__(self, other):
        if not self.__class__ in other.__class__.mro():
            return False
        else:        
            return (self.x == other.x and self.y == other.y and self.z == other.z)

    def __repr__(self):
        return 'Vec3({}, {}, {})'.format(self.x, self.y, self.z)  