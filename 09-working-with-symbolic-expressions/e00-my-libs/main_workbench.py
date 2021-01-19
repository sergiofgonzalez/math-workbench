from my_expressions_v2 import *
from math import sin

expr = Power(Variable('x'), Number(2))
print(expr._python_expr())

print(expr.python_function(x=3))


expr=Product(
    Sum(
        Product(
            Number(3),
            Power(Variable('x'), Number(2))
        ),
        Variable('x')
    ),
    Apply(Function('sin'), Variable('x'))
)
print(expr._python_expr())

print(expr.python_function(x=3))

def f(x):
    return (3 * x **2 + x) * sin(x)

print(f(3))
