# draw and Points will be brought into scope with 'import *'
from vector_drawing import *

dino_vectors = [(-5, 1), (-5, 2), (-5, 3), (-4, 0),
                (-4, 4), (-3, 4), (-2, 1), (-2, 2),
                (-2, 5), (-1, -4), (-1, 0), (-1, 5),
                (0, -3), (0, 0), (1, -4), (1, -2),
                (1, 2), (2, -3), (3, -1), (3, 1),
                (5, 1), (6, 4)]

sorted_dino_vectors = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4), (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0),
                        (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)]

# draw(
#   Points(*dino_vectors),
#   Segment((6, 4), (3, 1)),
#   Segment((3, 1), (1, 2))
#   )

# draw(Points(*sorted_dino_vectors))

def get_dino_segments(*vectors):
  segments = []
  start = vectors[0]

  for v in vectors[1:-1]:
    segments.append(Segment(start, v))
    start = v

  segments.append(Segment(v, vectors[-1]))
  segments.append(Segment(vectors[-1], vectors[0]))
  return segments


segments = get_dino_segments(*sorted_dino_vectors)
draw(Points(*sorted_dino_vectors), *segments)


