def parse_natural_numbers(a, b):
    if a is None or b is None:
        raise ValueError("a and b are required")

    if isinstance(a, bool) or isinstance(b, bool):
        raise ValueError("boolean values are not allowed")

    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a and b must be integers")

    if a < 0 or b < 0:
        raise ValueError("a and b must be natural numbers")

    return a, b
