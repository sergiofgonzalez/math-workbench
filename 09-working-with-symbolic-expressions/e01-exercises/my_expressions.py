# A collection of classes for representing algebraic expressions

# Added in section 10.1.3

## Elements
class Number():
    def __init__(self, number):
        self.number = number

class Variable():
    def __init__(self, symbol):
        self.symbol = symbol

# Combinators
class Power():
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

class Product():
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

class Sum():
    def __init__(self, *exprs):
        self.exprs = exprs

class Function():
    def __init__(self, name):
        self.name = name

class Apply():
    def __init__(self, function, argument):
        self.function = function
        self.argument = argument

# Added in exercise 10.4
class Quotient():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

# Added in exercise 10.5
class Difference():
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

# Added in exercise 10.6
class Negative():
    def __init__(self, expr):
        self.expr = expr