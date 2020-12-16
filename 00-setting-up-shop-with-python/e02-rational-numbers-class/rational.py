from math import gcd

class Rational():

    def __init__(self, numerator, denominator=1):
        if not Rational.__isValidIntsInts(numerator, denominator):
            raise TypeError('Rational expects integer arguments')

        if denominator == 0:
            raise ValueError('Rational expects non-zero denominator')

        greatest_common_divisor = gcd(abs(numerator), abs(denominator))


        self.numerator = numerator // greatest_common_divisor
        self.denominator = denominator // greatest_common_divisor

    def add(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError('Rational.add expects an integer or Rational')

        otherRational = other
        if isinstance(other, int):
            otherRational = Rational(other)

        return Rational(self.numerator * otherRational.denominator + otherRational.numerator * self.denominator, self.denominator * other.denominator)

    def mult(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError('Rational.add expects an integer or Rational')

        otherRational = other
        if isinstance(other, int):
            otherRational = Rational(other)

        return Rational(self.numerator * otherRational.numerator, self.denominator * otherRational.denominator)

    def div(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError('Rational.add expects an integer or Rational')

        otherRational = other
        if isinstance(other, int):
            otherRational = Rational(other)

        return self.mult(Rational(otherRational.denominator, otherRational.numerator))

    def subtract(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError('Rational.add expects an integer or Rational')

        otherRational = other
        if isinstance(other, int):
            otherRational = Rational(other)

        return self.add(otherRational.mult(-1))

    def lessThan(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError('Rational.add expects an integer or Rational')

        otherRational = other
        if isinstance(other, int):
            otherRational = Rational(other)

        return self.numerator * otherRational.denominator < otherRational.numerator * self.denominator

    def lessOrEqualThan(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError('Rational.add expects an integer or Rational')

        otherRational = other
        if isinstance(other, int):
            otherRational = Rational(other)

        return self.numerator * otherRational.denominator <= otherRational.numerator * self.denominator

    def greaterThan(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError('Rational.add expects an integer or Rational')

        otherRational = other
        if isinstance(other, int):
            otherRational = Rational(other)

        return self.numerator * otherRational.denominator > otherRational.numerator * self.denominator

    def greaterThanOrEqual(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError('Rational.add expects an integer or Rational')

        otherRational = other
        if isinstance(other, int):
            otherRational = Rational(other)

        return self.numerator * otherRational.denominator >= otherRational.numerator * self.denominator

    def power(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError('Rational.power expects integer exponent')

        return Rational(self.numerator ** exponent, self.denominator ** exponent)

    def __add__(self, other):
        return self.add(other)

    def __rsub__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError('Rational.rsub expects an integer or Rational')

        otherRational = other
        if isinstance(other, int):
            otherRational = Rational(other)

        return otherRational.subtract(self)

    def __radd__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError('Rational.radd expects an integer or Rational')

        otherRational = other
        if isinstance(other, int):
            otherRational = Rational(other)

        return otherRational.add(self)

    def __neg__(self):
        return self.mult(-1)

    def __mul__(self, other):
        return self.mult(other)

    def __rmul__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError('Rational.add expects an integer or Rational')

        otherRational = other
        if isinstance(other, int):
            otherRational = Rational(other)

        return otherRational.mult(self)

    def __sub__(self, other):
        return self.subtract(other)

    def __truediv__(self, other):
        return self.div(other)

    def __eq__(self, other):
        if not self.__class__ in other.__class__.mro():
            return False
        else:
            return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.lessThan(other)

    def __le__(self, other):
        return self.lessOrEqualThan(other)

    def __gt__(self, other):
        return self.greaterThan(other)

    def __ge__(self, other):
        return self.greaterThanOrEqual(other)

    def __pow__(self, exponent):
        return self.power(exponent)

    def __repr__(self):
        if self.numerator == 0:
            return 0
        elif self.denominator == 1:
            return self.numerator
        else:
            return '{}/{}'.format(self.numerator, self.denominator)

    @staticmethod
    def __isValidIntsInts(*nums):
        return all([isinstance(num, int) for num in nums])


