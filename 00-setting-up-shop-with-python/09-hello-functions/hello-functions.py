# Simple function definition: note that indentation is required
def square(x):
  y = x * x
  return y

print(square(5))

# function with several explicit arguments
def add3(x, y, z):
  return x + y + 3

print(1 + 2 + 3)

# function that takes a variable number of arguments: * means take all the args and put them in a tuple
def add(*args):
  total = 0
  for num in args:
    total += num
  return total

print(add(1, 2, 3, 4, 5))
print(add())
# print(add([1, 2, 3]))  # TypeError: unsupported operand type

# * can also be used to take a list and convert it into something that can be fed into *args
nums = [1, 2, 3, 4, 5]
print(add(*nums))

# using named arguments
def birthday(name="friend", age=None):
  s = "Happy birthday, %s" % name
  if age:
    s += ", you are %d years old" % age
  return s + "!"

print(birthday())
print(birthday("Alex"))
print(birthday("Alex", 4))
print(birthday(name="Alex", age=4))
print(birthday(age=4, name="Alex"))
print(birthday(age=4))

# arguments can be packed into a dictionary, and then passed to the function with **
nephew={ "name": "Alex", "age": 4}
print(birthday(**nephew))

# Also, function can be defined to receive an unstructured dictionary
def birthday_v2(**kwargs):
  s = "Happy birthday, %s" % kwargs["name"] if "name" in kwargs else "friend"
  if "age" in kwargs:
    s += ", you're %d years old" % kwargs["age"]
  return s + "!"

print(birthday_v2(name="Alex", age=4))
print(birthday_v2(age=4, name="Alex"))
print(birthday_v2(age=4))


# Functions are first-class citizens in Python
def evaluate(f, x):
  return f(x)

print(evaluate(square, 10))

# And the usual higher-order functions are there: map, filter, reduce
squares = map(square, range(0, 10))
print(squares)
print(list(squares))

nums = range(0, 20)
even_nums = filter(lambda n: n % 2 == 0, nums)
print(list(even_nums))

from functools import reduce
def sum_fn(x, y):
  print("x=%d, y=%d" % (x, y))
  return x + y
sum = reduce(sum_fn, nums)
print(sum)

sum = reduce(lambda acc, n: acc + n, nums)
print(sum)

# Also: you can return functions from functions, closures works as in JavaScript
def make_power_function(power):
  def power_fn(x):
    return x ** power
  return power_fn

square_fn = make_power_function(2)
print(list(map(square_fn, range(0, 10))))

cube_fn = make_power_function(3)
print(list(map(cube_fn, range(0, 10))))

# lambdas
fn = lambda x: x + 2
print(fn(5))

print((lambda x: x + 3)(5))

print((lambda x, y: x + y)(2, 3))

add2 = lambda x, y: x + y
print(add2(2, 3))

def make_power_fn(power):
  return lambda base: base ** power

power4 = make_power_fn(4)
print(list(map(power4, range(0, 10))))

def make_power_sequence(base):
  return lambda power: base ** power

print(list(map(make_power_sequence(2), range(0, 16))))

print(list(map(lambda x: x + 2, range(0, 10))))

# sometimes list comprehension are more readable than list(lambda...)
print([x + 2 for x in range(0, 10)])

#
## Applying functions to NumPy arrays
#
import numpy as np

# sqrt can be applied to a NumPy array (i.e. sqrt will be applied to each item of the array)
print(np.sqrt(np.arange(0, 10)))

# you can use `vectorize` to create a custom function that can be applied to each item of a NumPy array
def my_custom_function(x):
  if x % 2 == 0:
    return x/2
  else:
    return 0

my_numpy_function = np.vectorize(my_custom_function)
print(my_numpy_function(np.arange(0, 10)))