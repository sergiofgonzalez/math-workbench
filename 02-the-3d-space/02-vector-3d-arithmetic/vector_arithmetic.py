# A collection of supporting functions for Vector Arithmetic
from math import sqrt


def add(*vectors):
  """Return vector sum resulting of adding the given vectors

  The vectors must be given in their Cartesian coordinates.
  """
  by_coordinate_list = zip(*vectors)
  sum_by_coordinate_list = [sum(coords) for coords in by_coordinate_list]
  return tuple(sum_by_coordinate_list)

def subtract(v, w):
  """Return the vector resulting from subtracting w from v

  The vectors must be given in their Cartesian coordinates.
  """
  return tuple( v[i] - w[i] for i in range(0, len(v)) )

def scalar_product(factor, v):
  """Return the vector resulting from multiplying input scalar times the input vector.

  Factor is any real number, and v is a vector given in their Cartesian coordinates.
  """
  return tuple( factor * v_i for v_i in v )

def length(v):
  """Return the length of the vector

  v is a vector given in their Cartesian coordinates.
  """
  return sqrt(sum([ v_i ** 2 for v_i in v]))