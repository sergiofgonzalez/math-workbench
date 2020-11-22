from vector import Vector

class LinearFunction(Vector):

    def __init__(self, a, b):
        if not (isinstance(a, (int, float)) and (b, isinstance(int, float))):
            raise TypeError('LinearFunction expects numeric coefficients')
        self.a = a
        self.b = b

    def add(self, other):        
        return LinearFunction(self.a + other.a, self.b + other.b)

    def scale(self, scalar):
        return LinearFunction(self.a * scalar, self.b * scalar)

    @classmethod
    def zero(cls):
        return LinearFunction(0, 0)


    def __eq__(self, other):
        if not self.__class__ in other.__class__.mro():
            return False
        else:
            return (self.a == other.a and self.b == other.b)

    def __repr__(self):
        return 'LinearFunction(x: {}*x + {})'.format(self.a, self.b)  

    def __call__(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError('LinearFunction.__call__: requires a numeric argument') 

        return self.a * x + self.b
