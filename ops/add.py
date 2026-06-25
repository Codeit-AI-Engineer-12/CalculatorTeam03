from ops.parser import parse_natural_numbers


def add(a=None, b=None):
    a, b = parse_natural_numbers(a, b)
    return a + b
