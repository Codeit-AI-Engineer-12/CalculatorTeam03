def multiply(a: int, b: int) -> int | None:
    """int형 두 수를 곱합니다

    Args:
        a (int): int형 숫자
        b (int): int형 숫자

    Returns:
        int: a와 b를 곱한 값
        None: a나 b가 정상적인 값이 아닐 경우
    """
    if not isinstance(a, int) or not isinstance(b, int):
        print("입력되는 두 수 모두 int형이어야 합니다")
        return None
    if a < 0 or b < 0:
        print("자연수만 다룹니다. 흐즈믈르그")
        return None
    return a * b
