# A collection of classes for representing algebraic expressions
from abc import ABC, abstractmethod
import math

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

    # added in section 10.2.3
    @abstractmethod
    def expand(self):
        pass

    # added in exercise 10.12
    @abstractmethod
    def __repr__(self):
        pass

## Elements
class Number(Expression):
    def __init__(self, number):
        self.number = number

    def evaluate(self, **bindings):
        return self.number

    def expand(self):
        return self

    def __repr__(self):
        return 'Number({})'.format(self.number)

class Variable(Expression):
    def __init__(self, symbol):
        self.symbol = symbol

    def evaluate(self, **bindings):
        try:
            return bindings[self.symbol]
        except:
            raise KeyError('Variable {} is not bound'.format(self.symbol))

    def expand(self):
        return self

    def __repr__(self):
        return 'Variable(\'{}\')'.format(self.symbol)

# Combinators
class Power(Expression):
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def evaluate(self, **bindings):
        return self.base.evaluate(**bindings) ** self.exponent.evaluate(**bindings)

    def expand(self):
        return self

    def __repr__(self):
        return 'Power({}, {})'.format(self.base, self.exponent)

class Product(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self, **bindings):
        return self.expr1.evaluate(**bindings) * self.expr2.evaluate(**bindings)

    def expand(self):
        expanded1 = self.expr1.expand()
        expanded2 = self.expr2.expand()
        if isinstance(expanded1, Sum):
            return Sum(*[Product(expr, expanded2).expand() for expr in expanded1.exprs])
        elif isinstance(expanded2, Sum):
            return Sum(*[Product(expanded1, expr) for expr in expanded2.exprs])
        else:
            return Product(expanded1, expanded2)

    def __repr__(self):
        return 'Product({}, {})'.format(self.expr1, self.expr2)

class Sum(Expression):
    def __init__(self, *exprs):
        self.exprs = exprs

    def evaluate(self, **bindings):
        return sum([expr.evaluate(**bindings) for expr in self.exprs])

    def expand(self):
        return Sum(*[expr.expand() for expr in self.exprs])

    def __repr__(self):
        return 'Sum({})'.format(', '.join(['{}'.format(expr) for expr in self.exprs]))

# Added in exercise 10.4
class Quotient(Expression):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self, **bindings):
        return self.numerator.evaluate(**bindings) / self.denominator.evaluate(**bindings)

    def expand(self):
        return self

    def __repr__(self):
        return 'Quotient({}, {})'.format(self.numerator, self.denominator)

# Added in exercise 10.5
class Difference(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self, **bindings):
        return self.expr1.evaluate(**bindings) - self.expr2.evaluate(**bindings)

    def expand(self):
        return self

    def __repr__(self):
        return 'Difference({}, {})'.format(self.expr1, self.expr2)

# Added in exercise 10.6
class Negative(Expression):
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, **bindings):
        return -self.expr.evaluate(**bindings)

    def expand(self):
        return self

    def __repr__(self):
        return 'Negative({})'.format(self.expr)


class Function():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Function('{}')".format(self.name)

class Apply(Expression):
    def __init__(self, function, argument):
        self.function = function
        self.argument = argument

    def evaluate(self, **bindings):
        return _function_bindings[self.function.name](self.argument.evaluate(**bindings))

    def expand(self):
        return Apply(self.function, self.argument.expand())

    def __repr__(self):
        return 'Apply({}, {})'.format(self.function, self.argument)

_function_bindings = {
    'sin': math.sin,
    'cos': math.cos,
    'ln': math.log,
    'sqrt': math.sqrt
}

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

# Added in exercise 10.9
def contains(expr, var):
    if isinstance(expr, Variable):
        return expr.symbol == var.symbol
    elif isinstance(expr, Number):
        return False
    elif isinstance(expr, Power):
        return contains(expr.base, var) or contains(expr.exponent, var)
    elif isinstance(expr, Product):
        return contains(expr.expr1, var) or contains(expr.expr2, var)
    elif isinstance(expr, Sum):
        return any([contains(sum_expr, var) for sum_expr in expr.exprs])
    elif isinstance(expr, Quotient):
        return contains(expr.numerator, var) or contains(expr.denominator, var)
    elif isinstance(expr, Difference):
        return contains(expr.expr1, var) or contains(expr.expr2, var)
    elif isinstance(expr, Negative):
        return contains(expr.expr, var)
    elif isinstance(expr, Apply):
        return contains(expr.argument, var)
    else:
        raise TypeError('Not a valid expression')

# Added in exercise 10.10
def distinct_functions(expr):
    if isinstance(expr, Variable):
        return set()
    elif isinstance(expr, Number):
        return set()
    elif isinstance(expr, Sum):
        return set().union(*[distinct_functions(inner_expr) for inner_expr in expr.exprs])
    elif isinstance(expr, Product):
        return distinct_functions(expr.expr1).union(distinct_functions(expr.expr2))
    elif isinstance(expr, Power):
        return distinct_functions(expr.base).union(distinct_functions(expr.exponent))
    elif isinstance(expr, Apply):
        return set([expr.function.name]).union(distinct_functions(expr.argument))
    elif isinstance(expr, Quotient):
        return distinct_functions(expr.numerator).union(expr.denominator)
    elif isinstance(expr, Difference):
        return distinct_functions(expr.expr1).union(expr.expr2)
    elif isinstance(expr, Negative):
        return distinct_functions(expr.expr)
    else:
        raise TypeError('Not a valid expression')

# Added in exercise 10.11
def contains_sum(expr):
    if isinstance(expr, Variable):
        return False
    elif isinstance(expr, Number):
        return False
    elif isinstance(expr, Power):
        return contains_sum(expr.base) or contains_sum(expr.exponent)
    elif isinstance(expr, Product):
        return contains_sum(expr.expr1) or contains_sum(expr.expr2)
    elif isinstance(expr, Sum):
        return True
    elif isinstance(expr, Quotient):
        return contains_sum(expr.numerator) or contains_sum(expr.denominator)
    elif isinstance(expr, Difference):
        return contains_sum(expr.expr1) or contains_sum(expr.expr2)
    elif isinstance(expr, Negative):
        return contains_sum(expr.expr)
    elif isinstance(expr, Apply):
        return contains_sum(expr.argument)
    else:
        raise TypeError('Not a valid expression')