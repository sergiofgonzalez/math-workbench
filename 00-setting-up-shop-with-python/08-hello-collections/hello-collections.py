#
##  lists
#

# creating and accessing
months = ["January", "February", "March"]
print(months[0])
print(months[2])

# unpacking elements from a list
jan, feb, march = months
print(jan)
print(march)

# concatenating lists
longlist = [1, 2, 3] + [4, 5, 6]
print(longlist)

# slicing lists
sublist = longlist[1:3]   # will return a sublist with elements 1 and 2
print(sublist)

# length of a list
print(len(months))
print(len(longlist))
print(len(sublist))

# getting the last element from a list
print(longlist[-1])
print(longlist[len(longlist) - 1])

# getting the one before last item
print(longlist[-2])

# slicing with negative indices
sublist = longlist[1:-1]  # get elems from the second to the last
print(sublist)

# lists of lists
list_of_lists = [[1,2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_lists)
print(list_of_lists[1][1]) # second element from second vector

# iterating over a list
for x in months:
  print('Month: ' + x)

# appending items to a list
nums = [ 1, 2, 3, 4, 5 ]
squares = []  # empty list
for n in nums:
  squares.append(n * n)
print(squares)

# list comprehensions: lets you iteratively building lists
cubes = [ x * x * x for x in nums]
print(cubes)

years = [ 2018, 2019, 2020 ]
combination = [ m + " " + str(y) for y in years for m in months ]
print(combination)

multilist_combination = [[m + " " + str(y) for y in years] for m in months] # iterate over months first, then over year
print(multilist_combination)

# using a nested for in which the range is fixed (this is useful for iterating over tuple indices)
some_tuples = [(x, i) for x in range(-1, 6) for i in [0, 1]]
print(some_tuples)

#
## ranges
#
print(range(5, 10)) # => range(5, 10)

for i in range(5, 10):
  print(i)

# materializing a range into a list (this is OK for small ranges)
resulting_list = list(range(0, 10))
print(resulting_list)

print(list(range(10)))      # by default starts from zero
print(list(range(-5, 5)))
print(list(range(0, 10, 3)))

#
## zipping two iterables
#
z = zip([1, 2, 3], ['a', 'b', 'c'])
print(z)
print(list(z)) # materializing the zip operation

#
## Generators: iterables that give you a way to create iterables that don't store all of their values at once.
#
def count():
  x = 0
  while True:
    yield x
    x += 1

print(count())
print(count())
print(count())

for i in count():
  if i > 1000:
    break
  else:
    print(i)


# another example
def count_v2(a, b):
  x = a
  while x < b:
    yield x
    x += 1

gen = count_v2(1, 10)
for i in gen:
  print(i)

print([x for x in count_v2(1, 10)])


#
## Generator comprehensions
#

# following code is the same as:
# def squares():
#   for x in range(0, 10)
#     yield x * x
gen_comprehension = (x * x for x in range(0, 10))
print(gen_comprehension)
for x in gen_comprehension:
  print(x)

# You can materialize a finite generator into a list
squares = list((x * x for x in range(0, 10)))
print(squares)

#
## tuples: immutable lists
#
print((1,2))
print(("a", "b", "c"))

my_tuple = 1, 2, 3, 4, 5
print(my_tuple)

# looks like tuple comprehension but it is actually a generator comprehension
# materialized as a tuple
a = 1, 2, 3, 4, 5
b = tuple(x + 10 for x in a)
print(b)


#
## Sets: collections where every entry must be distinct, and order is not important
#
import random
def genRandomInts(min, max, num_samples):
  x = 0
  while x < num_samples:
    yield random.randint(min, max)
    x += 1

nums = [ x for x in genRandomInts(1, 6, 20)]
print(nums)
print(set(nums))

#
## NumPy: it is the de-facto standard Python library for numerics. Many functions expect NumPy arrays as inputs.
#

import numpy as np


my_array = np.array([1, 2, 3, 4, 5, 6])
print(my_array)

print(np.arange(0, 10))
print(np.arange(0, 10, 0.1))


#
## Dictionaries: key-value maps
#
dog = {"name": "Mara", "age": 8}
print(dog["name"])
print(dog["age"])

# Obtaining an iterable of key-value pairs, and materializing them in a list
print(list(dog.items()))


#
## Some useful collection functions
#
print(sum([1, 2, 3]))
print(max([1, 2, 3]))
print(min([1, 2, 3]))
print(sorted([4, 3, 5, 2, 1]))
nums = [1, 2, 3, 4, 5]
print(reversed(nums))
print(nums) # original list has not been mutated