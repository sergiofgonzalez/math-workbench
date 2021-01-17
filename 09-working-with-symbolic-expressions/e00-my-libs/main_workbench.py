from my_expressions_v2 import *

expr = Product(
    Sum(
        Power(Product(Number(3), Variable('x')), Number(2)),
        Variable('x')),
    Apply(Function('sin'), Variable('x'))
)

print(expr)
print("Product(Sum(Power(Product(Number(3), Variable('x')), Number(2)), Variable('x')), Apply(Function('sin'), Variable('x')))")
