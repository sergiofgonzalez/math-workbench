# A collection of supporting functions for Vector Arithmetic
from math import sqrt, pi, acos


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

def scale(factor, v):
  """Return the vector resulting from scaling the input vector by the given factor.

  Factor is any real number, and v is a vector given in their Cartesian coordinates.
  Effectively, scale relies on the scalar_product.
  """
  return scalar_product(factor, v)


def length(v):
  """Return the length of the vector

  v is a vector given in their Cartesian coordinates.
  """
  return sqrt(sum([ v_i ** 2 for v_i in v]))

def dot_product(u, v):
  """Return the dot product of u with v

  u and v are vectors of any dimension given in their Cartesian coordinates.
  """
  return sum([coord1 * coord2 for coord1, coord2 in zip(u, v)])

def to_radians(degrees):
  """Return the radians value for the given value in degrees"""
  return (degrees * pi) / 180

def to_degrees(radians):
  """Return degrees value for the given value in radians"""
  return (radians * 180) / pi

def angle_between(u, v):
  """Return the angle between u and v

  u and v are vectors of any dimension given in their Cartesian coordinates.
  """
  return acos(dot_product(u, v) / (length(u) * length(v)))


def cross_product(u, v):
  """Return the cross product of u and v

  The vectors must be 3D vectors given in their Cartesian coordinates
  """
  ux, uy, uz = u
  vx, vy, vz = v
  return (uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx)