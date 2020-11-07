from vector import Vector

class Vec0(Vector):
    def __init__(self):
        pass

    @classmethod
    def zero(cls):
        return Vec0()

    def add(self, other):
        return Vec0()

    def scale(self, scalar):
        return Vec0()

    def __eq__(self, other):
        return self.__class__ == other.__class__

    def __repr__(self):
        return 'Vec0()'