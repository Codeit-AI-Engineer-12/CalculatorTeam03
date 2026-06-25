from utils.parser import parse_natural_numbers

def factorial(n):
    """
    n! (n 팩토리얼) 값을 반환합니다.
    """

    n = parse_natural_numbers(n)[0]
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result