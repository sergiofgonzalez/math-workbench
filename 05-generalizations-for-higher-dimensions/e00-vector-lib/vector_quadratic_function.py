from vector import Vector

class QuadraticFunction(Vector):

    def __init__(self, a, b, c):
        if not (isinstance(a, (int, float)) and (b, isinstance(int, float)) and (c, isinstance(int, float))):
            raise TypeError('LinearFunction expects numeric coefficients')
        self.a = a
        self.b = b
        self.c = c

    def add(self, other):        
        return QuadraticFunction(self.a + other.a, self.b + other.b, self.c + other.c)

    def scale(self, scalar):
        return QuadraticFunction(self.a * scalar, self.b * scalar, self.c * scalar)

    @classmethod
    def zero(cls):
        return QuadraticFunction(0, 0, 0)


    def __eq__(self, other):
        if not self.__class__ in other.__class__.mro():
            return False
        else:
            return (self.a == other.a and self.b == other.b and self.c == other.c)

    def __repr__(self):
        return 'QuadraticFunction(x: {}*x² + {}x + {})'.format(self.a, self.b, self.c)  

    def __call__(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError('QuadraticFunction.__call__: requires a numeric argument') 

        return self.a * (x ** 2) + self.b * x + self.c
