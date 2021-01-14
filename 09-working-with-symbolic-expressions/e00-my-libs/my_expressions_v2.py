# A collection of classes for representing algebraic expressions
from abc import ABC, abstractmethod

def to_expression_safe(maybeExpression):
    if isinstance(maybeExpression, Expression):
        return maybeExpression
    elif isinstance(maybeExpression, (int, float)):
        return Number(maybeExpression)
    else:
        raise ValueError('Cannot convert {} to Expression'.format(maybeExpression))

class Expression(ABC):
    @abstractmethod
    def evaluate(self, **bindings):
        pass

    def __neg__(self):
        return Negative(to_expression_safe(self))

    def __add__(self, other):
        return Sum(self, to_expression_safe(other))

    def __sub__(self, other):
        return Difference(self, to_expression_safe(other))

    def __mul__(self, other):
        return Product(self, to_expression_safe(other))

    def __rmul__(self, other):
        return Product(to_expression_safe(other), self)

    def __truediv__(self, other):
        return Quotient(self, to_expression_safe(other))

    def __pow__(self, exponent):
        return Power(self, to_expression_safe(exponent))



## Elements
class Number(Expression):
    def __init__(self, number):
        self.number = number

    def evaluate(self, **bindings):
        return self.number

class Variable(Expression):
    def __init__(self, symbol):
        self.symbol = symbol

    def evaluate(self, **bindings):
        try:
            return bindings[self.symbol]
        except:
            raise KeyError('Variable {} is not bound'.format(self.symbol))

# Combinators
class Power(Expression):
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

class Product(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

class Sum(Expression):
    def __init__(self, *exprs):
        self.exprs = exprs

class Function(Expression):
    def __init__(self, name):
        self.name = name

class Apply(Expression):
    def __init__(self, function, argument):
        self.function = function
        self.argument = argument

# Added in exercise 10.4
class Quotient(Expression):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

# Added in exercise 10.5
class Difference(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

# Added in exercise 10.6
class Negative(Expression):
    def __init__(self, expr):
        self.expr = expr

# Added in section 10.2.1
def distinct_variables(expr):
    """Returns a set with all the variables in the expression
    """
    if isinstance(expr, Variable):
        return set(expr.symbol)
    elif isinstance(expr, Number):
        return set()
    elif isinstance(expr, Sum):
        return set().union(*[distinct_variables(inner_expr) for inner_expr in expr.exprs])
    elif isinstance(expr, Product):
        return distinct_variables(expr.expr1).union(distinct_variables(expr.expr2))
    elif isinstance(expr, Power):
        return distinct_variables(expr.base).union(distinct_variables(expr.exponent))
    elif isinstance(expr, Apply):
        return distinct_variables(expr.argument)
    elif isinstance(expr, Quotient):
        return distinct_variables(expr.numerator).union(expr.denominator)
    elif isinstance(expr, Difference):
        return distinct_variables(expr.expr1).union(expr.expr2)
    elif isinstance(expr, Negative):
        return distinct_variables(expr.expr)
    else:
        raise TypeError('Not a valid expression')