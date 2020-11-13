from coordinate_vector import CoordinateVector

class Vec5(CoordinateVector):

    @classmethod
    def dimension(cls):
        return 5

    @classmethod
    def zero(cls):
        coords = tuple(0 for _ in range(0, cls.dimension()))
        return Vec5(*coords)
