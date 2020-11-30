# A collection of vector related functions
from math import sqrt, pi, acos, sin, cos, atan2


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

def length(v):
  """Return the length of the vector

  v is a vector given in their Cartesian coordinates.
  """
  return sqrt(sum([ v_i ** 2 for v_i in v]))

def dot(u, v):
  """Return the dot product of u with v

  u and v are vectors of any dimension given in their Cartesian coordinates.
  """
  return sum([coord1 * coord2 for coord1, coord2 in zip(u, v)])

def distance(v1, v2):
  """Return the distance between the given vectors

  The vectors must be given in their Cartesian coordinates.
  """
  return length(subtract(v2, v1))

def perimeter(vectors):
  """Return the perimeter of the polygon identified by the given vectors

  The vectors must be given in their Cartesian coordinates.
  """
  distances = [distance(vectors[i], vectors[(i + 1) % len(vectors)]) for i in range(0, len(vectors))]
  return sum(distances)

def scale(factor, v):
  """Return the vector resulting from scaling the input vector by the given factor.

  Factor is any real number, and v is a vector given in their Cartesian coordinates.
  Effectively, scale relies on the scalar_product.
  """
  return tuple(factor * coord for coord in v)

def to_cartesian(polar_vector):
  """Return the Cartesian coordinates of the given vector

  The given vector must be specified using polar coordinates
  """
  length, angle = polar_vector[0], polar_vector[1] # this is like destructuring
  return (length * cos(angle), length * sin(angle))

def translate(translation_vector, vectors):
  """Returns the vectors translated according to the given translation vector

  The translation vector and the vectors must be given in their Cartesian coordinates.
  """
  return [add(translation_vector, v) for v in vectors]

def rotate2d(rotation_angle, vector):
  """Return the vector that results from rotating the given vector by the provided angle

  The rotation angle must be given in radians, and the vector must be a 2D vector
  specified using its Cartesian coordinates
  """
  vector_length, vector_angle = to_polar(vector)
  new_vector_angle = vector_angle + rotation_angle
  return to_cartesian((vector_length, new_vector_angle))

def rotate2d_multiple(rotation_angle, vectors):
  """Return the list of vectors rotated by the given angle

  The rotation angle must be given in radians, and the vectors must be 2D vectors
  specified using their Cartesian coordinates
  """
  vectors_polar = [to_polar(v) for v in vectors]
  rotated_vectors_polar = [ (v[0], v[1] + rotation_angle) for v in vectors_polar]
  rotated_vectors = [to_cartesian(v) for v in rotated_vectors_polar]
  return rotated_vectors

def to_polar(vector):
  """Return the polar coordinates of the given vector

  The given vector must be given in Cartesian coordinates
  """
  x, y = vector[0], vector[1] # destructuring
  angle = atan2(y, x)
  return (length(vector), angle)

def angle_between(u, v):
  """Return the angle between u and v

  u and v are vectors of any dimension given in their Cartesian coordinates.
  """
  return acos(dot(u, v) / (length(u) * length(v)))

def cross(u, v):
  """Return the cross product of u and v

  The vectors must be 3D vectors given in their Cartesian coordinates
  """
  ux, uy, uz = u
  vx, vy, vz = v
  return (uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx)

def to_radians(degrees):
  """Return the radians value for the given value in degrees"""
  return (degrees * pi) / 180

def to_degrees(radians):
  """Return degrees value for the given value in radians"""
  return (radians * 180) / pi

def component(v, direction):
  """Return the component of v in the given direction.

  The vector and the direction must be given in their Cartesian coordinates
  For example `component((1, 2, 3), (0, 0, 1)) => 3`
  """
  return (dot(v, direction) / length(direction))

def unit(v):
  """Return a vector on the same direction as the one given, but with length equal to one

  The vector must be given in its Cartesian coordinates.
  """
  return scale(1. / length(v), v)
