from vector_drawing import *

dino_points = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4), (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0),
                        (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)]

# drawing a polygon with default options
draw(Polygon(*dino_points))

# drawing a polygon with default options for the polygon but no axes
draw(Polygon(*dino_points), axes=None)

# drawing a polygon with default options for the polygon but no grid
draw(Polygon(*dino_points), grid=None)

# drawing a polygon with default options for the polygon but no origin
draw(Polygon(*dino_points), origin=None)

# drawing a polygon with default options and non-default width (larger)
draw(Polygon(*dino_points), width=10)

# drawing a polygon with default options and non-default aspect ratio
draw(Polygon(*dino_points), nice_aspect_ratio=False)


# drawing a polygon with default options for the polygon and non-default grid
draw(Polygon(*dino_points), grid=(2, 2))

# drawing a polygon with perimeter in black, fill in blue with default alpha blending
draw(Polygon(*dino_points, color=black, fill=blue))

# drawing a polygon with perimeter in black, fill in blue with less transparency
draw(Polygon(*dino_points, color=black, fill=blue, alpha=0.8))

# drawing default points
draw(Points(*dino_points))

# drawing default points in non-default color
draw(Points(*dino_points, color=blue))

# drawing some arrows
draw(Arrow(dino_points[0]))

draw(Arrow(dino_points[0], dino_points[1]))

# drawing some segments
draw(Segment(dino_points[0], dino_points[1]))