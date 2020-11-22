from vector import Vector

class Function2(Vector):

    def __init__(self, f):
        if not callable(f):
            raise TypeError('Function expects a function object')

        self.f = f

    def add(self, other):        
        def add_fn(x, y):
            return self.f(x, y) + other.f(x, y)
        return Function2(add_fn)


    def scale(self, scalar):
        def scalar_mult_fn(x, y):
            return scalar * self.f(x, y)
        return Function2(scalar_mult_fn)

    @classmethod
    def zero(cls):
        def zero_fn(x, y):
            return 0
        return zero_fn

    def __call__(self, x, y):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise TypeError('Function2.__call__: requires a numeric argument') 

        return self.f(x, y)
