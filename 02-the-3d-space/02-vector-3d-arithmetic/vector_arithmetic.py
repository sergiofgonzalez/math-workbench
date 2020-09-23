# A collection of supporting functions for Vector Arithmetic

def add(*vectors):
  """Return vector resulting of adding the given vectors

  The vectors must be given in their Cartesian coordinates.
  """
  by_coordinate_list = zip(*vectors)
  sum_by_coordinate_list = [sum(coords) for coords in by_coordinate_list]
  return tuple(sum_by_coordinate_list)