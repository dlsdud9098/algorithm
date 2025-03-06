def solution(n):
    import math
    answer = 0
    
    # 루트를 씌우고 정수형으로 변환
    sqrt_num = int(math.sqrt(n))
    # 바꾼 정수형을 제곱했을 때 기존의 n과 같으면 계산하여 리턴
    if sqrt_num ** 2 == n:
        answer = (sqrt_num + 1) **2
    else:
        answer = -1
    return answer