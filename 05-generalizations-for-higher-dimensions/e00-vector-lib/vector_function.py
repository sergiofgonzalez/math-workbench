from vector import Vector

class Function(Vector):

    def __init__(self, f):
        if not callable(f):
            raise TypeError('Function expects a function object')

        self.f = f

    def add(self, other):        
        def add_fn(x):
            return self.f(x) + other.f(x)
        return Function(add_fn)


    def scale(self, scalar):
        def scalar_mult_fn(x):
            return scalar * self.f(x)
        return Function(scalar_mult_fn)

    @classmethod
    def zero(cls):
        def zero_fn(x):
            return 0
        return zero_fn

    def __call__(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError('Function.__call__: requires a numeric argument') 

        return self.f(x)
