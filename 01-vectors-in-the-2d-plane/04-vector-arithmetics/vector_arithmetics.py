from math import sqrt, sin, cos, pi, atan2

def length(v):
  """Return the length of a vector in the 2D plane

  v must be specified in Cartesian coordinates
  """
  return sqrt(v[0] ** 2 + v[1] ** 2)

def add(*vectors):
  """Return the result of adding the given vectors

  vectors must be specified in Cartesian coordinates
  """
  return (sum([v[0] for v in vectors]), sum([v[1] for v in vectors]))

def negate(v):
  """Negate the given v vector

  v must be specified in Cartesian coordinates
  """
  return (-v[0], -v[1])

def subtract(v1, v2):
  """Return the result of subtracting the vector v1 from v2

  v1 and v2 must be given in Cartesian coordinates
  """
  return add(v1, negate(v2))

def scalar_product(scalar, vector):
  """Return the result of multiplying the scalar by the vector

  scalar is a real number, vector must be specified in Cartesian coordinates
  """
  return (scalar * vector[0], scalar * vector[1])


def to_cartesian(polar_vector):
  """Return the Cartesian coordinates of the given vector

  The given vector must be specified using polar coordinates
  """
  length, angle = polar_vector[0], polar_vector[1] # this is like destructuring
  return (length * cos(angle), length * sin(angle))

def to_radians(degrees):
  """Return the radians value for the given value in degrees"""
  return (degrees * pi) / 180

def to_degrees(radians):
  """Return degrees value for the given value in radians"""
  return (radians * 180) / pi

def to_polar(vector):
  """Return the polar coordinates of the given vector

  The given vector must be given in Cartesian coordinates
  """
  x, y = vector[0], vector[1] # destructuring
  angle = atan2(y, x)
  return (length(vector), angle)


def translate(translation_vector, vectors):
  """Returns the vectors translated according to the given translation vector

  The translation vector and the vectors must be given in their Cartesian coordinates.
  """
  return [add(translation_vector, v) for v in vectors]

def scale(s, vectors):
  """Return the vectors scale by the given factor

  The vectors must be specified in their Cartesian coordinates
  """
  return [scalar_product(s, v) for v in vectors]

def rotate(rotation_angle, vectors):
  """Return the vectors rotated by the given angle

  The rotation angle must be given in radians, and the vectors must be
  specified using their Cartesian coordinates
  """
  vectors_polar = [to_polar(v) for v in vectors]
  rotated_vectors_polar = [ (v[0], v[1] + rotation_angle) for v in vectors_polar]
  rotated_vectors = [to_cartesian(v) for v in rotated_vectors_polar]
  return rotated_vectors

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