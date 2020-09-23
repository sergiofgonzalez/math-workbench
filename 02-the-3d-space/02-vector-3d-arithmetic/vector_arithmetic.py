# A collection of supporting functions for Vector Arithmetic

def add(*vectors):
  """Return vector resulting of adding the given vectors

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
  """
  Return the vector resulting from multiplying the scalar factor by the vector v

  Factor is any real number, and v is a vector given in their Cartesian coordinates.
  """
  return tuple( factor * v_i for v_i in v )

