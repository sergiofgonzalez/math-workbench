def standard_form(v1, v2):
    """Return the coefficients of the standard form line
    that passes through the points v1 and v2
    """
    if len(v1) != 2  or len(v2) != 2:
        raise TypeError('standard_form expects 2D vectors')

    if not all([
        isinstance(v1[0], (int, float)), isinstance(v1[1], (int, float)),
        isinstance(v2[0], (int, float)), isinstance(v2[1], (int, float))]):
        raise TypeError('standard_form expects numeric coordinates')

    x1, y1 = v1
    x2, y2 = v2
    a = y2 - y1
    b = x1 - x2
    c = x1 * y2 - y1 * x2
    return (a, b, c)


