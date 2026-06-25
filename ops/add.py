def add(a=None, b=None):
    if a is None or b is None:
        raise ValueError("a and b are required")

    if isinstance(a, bool) or isinstance(b, bool):
        raise ValueError("boolean values are not allowed")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("a and b must be numeric")

    return a + b
