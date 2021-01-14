
def f(**args):
    print(args)


f(x=1, y=2, z=3)

# from my_expressions_v2 import *

# expr = 2 * Variable('x') + 3

# print(distinct_variables(expr))

# f = Product(
#     Sum(
#         Product(
#             Number(3),
#             Power(Variable('x'), Number(2))
#         )
#         ,
#         Variable('x')
#     ),
#     Apply(Function('sin'), Variable('x'))
# )

# print(distinct_variables(f))
