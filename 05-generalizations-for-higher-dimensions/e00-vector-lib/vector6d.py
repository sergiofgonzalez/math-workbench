from coordinate_vector import CoordinateVector

class Vec6(CoordinateVector):

    @classmethod
    def dimension(cls):
        return 6

    @classmethod
    def zero(cls):
        coords = tuple(0 for _ in range(0, cls.dimension()))
        return Vec6(*coords)
