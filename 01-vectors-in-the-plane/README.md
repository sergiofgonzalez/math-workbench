# 01 &mdash; Vectors in the 2D Plane
> (TBD)

## Introduction
Models of 2D entities are important in programming. Anything that shows up on the screen is a 2D object occupying some width and height of pixels.

Vectors are objects that live in multi-dimensional spaces. They have their own notions of arithmetic (adding, multiplying, and so on). This sections deals with 2D vectors.

The 2D world is referred to as *plane* and objects living in a 2D plane has two dimensions: width and height. Locations in the plane are identified by their vertical and horizontal positions, typically referred to a reference point: the *origin* of the plane.

A 2D vector is a point in the plane relative to the origin. 2D vectors are represented laying out in the plane two perpendicular axes that intersect at the origin of the plane. The horizontal axis is called the *x-axis* and the vertical one is called the *y-axis*.

Points in the plane are represented by their position with respect with those axes, for example `(6, 4)` which represent the value of the *x* and *y* coordinates of the point.

## Drawing in 2D using Python
We will be using a small set of custom-built functions to create drawings, built on top of `Matplotlib`.

The following table lists some Python classes representing geametric figures, usable with a function called `draw` that takes as input these classes.

| Class | Constructor Example | Description |
| :---- | :------------------ | :---------- |
| `Polygon` | `Polygon(*vectors)` | Draws a polygon whose vertices are represented by a list of vectors. |
| `Points` | `Points(*vectors)` | Represent a list of points to draw. |
| `Arrow` | `Arrow(tip, [tail])` | Draws an arrow from the origin to the tip of the vector, or from the tail vector to the tip vector if `tail` is given. |
| `Segment` | `Segment(start, end)` | Draws a line segment from the start vector to the end vector. |

