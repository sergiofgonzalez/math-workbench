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

The following table lists some Python classes representing geametric figures, usable with a function called `draw()` that takes as input these classes.

| Class | Constructor Example | Description |
| :---- | :------------------ | :---------- |
| `Polygon` | `Polygon(*vectors)` | Draws a polygon whose vertices are represented by a list of vectors. |
| `Points` | `Points(*vectors)` | Represent a list of points to draw. |
| `Arrow` | `Arrow(tip, [tail])` | Draws an arrow from the origin to the tip of the vector, or from the tail vector to the tip vector if `tail` is given. |
| `Segment` | `Segment(start, end)` | Draws a line segment from the start vector to the end vector. |

There are few extra options you can pass to the `draw()` function:

+ `grid=(x_unit, y_unit)` &mdash; use x_unit, y_unit values for each of the x-axis and y-axis unit step
+ `nice_aspect_ratio` &mdash; instructs `draw()` not to keep the x-axis and y-axis scales the same

## Plane Vector Arithmetic
Like numbers, vectors have their own kind of arithmetic. Note that operations from vector arithmetic accomplish useful geometric transformations that can be visualized in the 2D plane.

### Vector Addition
Given two input vectors:

```
v1 = (v1_x, v1_y)
v2 = (v2_x, v2_y)

v1 + v2 = (v1_x + v2_x, v1_y + v2_y)
```

The rule for vector addition is sometimes called *tip-to-tail* addition because if you move the tail of the second vector to the tip of the first the sum is the arrow from the start of the first vector to the end of the second.

That is, adding a vector has the effect of moving (*translating* in Maths terms)

### Vector Components and Lengths
Many times it's usefult to decompose a vector as a sum of other vectors. For example, when using walk directions it is easier to say "*go 4 blocks east, then 3 blocks north*" rather than "*go 800 meters northeast*".

As an example, the vector `(4, 3)` can be represented as `(4, 0) + (0, 3)` which are called the x and y components of the `(4, 3)` vector.

The length of the vector is the length of the arrow that represents it, that is, the distance from the origin of the plane to the point that represents it.

If we recall the *Pythagorean theorem*:
> For a right triangle (a triangle having two sides meeting at a 90°), the square of the length of the longest side (hypotenuse) is the sum of the squares of the lengths of the other two sides.

Therefore, the length of the vector `(4, 3)` would be `√(4^2 + 3^2)

### Multiplying Vectors by Numbers
Repeated addition of vectors in *unambiguous*: you can keep stacking vectors using the *tip-to-tail* method as required.

The effect of adding a vector to itself a certain number of times can be represented as the product of multiplying a vector by a number. This is called *scalar multiplication*, as ordinary numbers are often called *scalars*. Also, *scalar* resembles *scale* and that's exactly the geometry interpretation of the *scalar product*: multiplying a given vector `v` by 2.5 scales `v` 2.5 times.

It is also interesting the fact that *scalar multiplication* of a vector scales both components by the same factor.
That is:

```
v = (a, b) = (a, 0) + (0, b)
r * v = r*(a, b) = (r*a, r*b) = (r*a, 0) + (0, r*b) = r*(a, 0) + r*(0, b)
```

This is true for any `r` including negative numbers, who have the effect of changing the direction of the vector to the opposite of the original one.

### Subtraction, displacement, and distance
Given a vector `v`, the negative vector `-v`, is the same as the scalar product `-1 * v`. Thus, `(-4, 3)` is the opposite of `(4, -3)`. The length of both `v` and `-v` will have the same length, but will point in the opposite direction.

*Vector subtraction* can be defined as:
`v - w = v + (-w)`

In geometry terms, `v - w` is the position of `v` relative to `w`.

In terms of coordinates, subtraction can be defined as:
```
v = (a, b), w = (c, d)
v - w = (a - c, b - d)