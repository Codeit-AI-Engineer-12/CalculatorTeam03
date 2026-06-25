def power(a: float, b: float) -> float:
     """
    두 자연수 a와 b를 입력받아 a의 b제곱 값을 반환합니다.

    Args:
        a: 밑이 되는 자연수
        b: 지수가 되는 자연수

    Returns:
        a의 b제곱 결과

    Raises:
        ValueError: a 또는 b가 음수이거나, 0의 0제곱인 경우
    """
     
     if a < 0 or b < 0:
        raise ValueError("자연수만 입력할 수 있습니다.")
        
     if a == 0 and b == 0:
        raise ValueError("0의 0제곱은 정의하지 않습니다.")
     
     return a ** b