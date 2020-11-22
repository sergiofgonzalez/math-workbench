from vector import Vector
from my_vectors import add, scale
from abc import abstractmethod

class Polynomial(Vector):

    @classmethod
    def zero(cls):
        return Polynomial(0)

    def __init__(self, *coefficients):
        if len(coefficients) < 0:
            raise TypeError('Polynomial constructor was expecting at least one coefficient')

        self.coefficients = coefficients

    def add(self, other):
        # we need to make self and other of the same size otherwise zip won't work

        if len(self.coefficients) >= len(other.coefficients):
            extra = [0 for _ in range(len(other.coefficients), len(self.coefficients))]
            p = list(other.coefficients) + extra            
            return Polynomial(*[a + b for a, b in zip(self.coefficients, p)])
        else:
            extra = [0 for _ in range(len(self.coefficients), len(other.coefficients))]
            p = list(self.coefficients) + extra            
            return Polynomial(*[a + b for a, b in zip(p, other.coefficients)])

    def scale(self, scalar):
        return Polynomial([a * scalar for a in self.coefficients])

    def __repr__(self):
        if len(self.coefficients) == 1:
            return '{}'.format(self.coefficients[0])
        elif len(self.coefficients) == 2:
            monomial_1 = '{}'.format(self.coefficients[0])
            monomial_2 = '{}x'.format(self.coefficients[1])
            return ' + '.join([monomial_1, monomial_2])
        else:
            monomial_1 = '{}'.format(self.coefficients[0])
            monomial_2 = '{}x'.format(self.coefficients[1])
            other_monomials = ['{}x^{}'.format(self.coefficients[i], i) for i in range(2, len(self.coefficients))]
            monomials = [monomial_1, monomial_2] + other_monomials
            return ' + '.join(monomials)

    def __eq__(self, other):
        if not self.__class__ in other.__class__.mro():
            return False
        else:        
            return self.coefficients == other.coefficients

    def __call__(self, x):
        return sum(coefficient * x ** power for (power, coefficient) in enumerate(self.coefficients))