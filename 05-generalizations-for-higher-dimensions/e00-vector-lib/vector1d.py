from vector import Vector

class Vec1(Vector):
    def __init__(self, x):
        self.x = x

    @classmethod
    def zero(cls):
        return Vec1(0)

    def add(self, other):
        return Vec1(self.x + other.x)

    def scale(self, scalar):
        return Vec1(scalar * self.x)

    def __eq__(self, other):
        if not self.__class__ in other.__class__.mro():
            return False
        else:
            return self.x == other.x

    def __repr__(self):
        return 'Vec1({})'.format(self.x) 