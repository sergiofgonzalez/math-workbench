# My Implementation
> the libraries and support functions used in the chapter, but implemented by me


## Description

+ `testing_my_impls.py` &mdash; the main program to test the libs and functions
+ `draw_model_custom_impl.py` &mdash; exports a very simple `draw_model_animate(...)` that exposes a function that draws the given triangles. It also enables very basic animation so that you can see the whole shape (using `a` to start animating, `s` to stop animating, and the left right mouse buttons)
+ `transformations_support.py` &mdash; my implementation of the given transformations such as `scale_by(...)`, `translate_by(...)`, `rotate_*_by(...)`.
+ `vectors_my_implementation.py` &mdash; vector supporting functions to add vectors, cross product, etc.
+ `my_colors.py` &mdash; fixes on `colors.py` as it didn't work for orange color.
+ `my_draw2d.py` &mdash; simple customization of `draw2d.py` that uses `my_colors.instead`.

+ `teapot.off` &mdash; The Utah teapot 3D model as an *off* file (original from the author)
+ `teapot.py` &mdash; Support functions such as `load_triangles(...)` used to draw the Utah teapot (original from the author)

Remember that you run the project you must do:
```bash

$ pwd
[...]/03-transformations/e03-my-implementation

# it must be run within the project directory so that teapot.off is found
$ python3 testing_my_impls.py
```
