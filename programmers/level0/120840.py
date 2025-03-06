def solution(balls, share):
    answer = 0
    
    # 경우의 수 계산 식
    # balls ! / (balls - share)! * (share)!
    
    # (balls - share)!
    f_b_s = 1
    for i in range(1, balls-share+1):
        f_b_s  *= i
    
    # share!
    f_s = 1
    for i in range(1, share+1):
        f_s *= i
    
    # balls!
    f_b = 1
    for i in range(1, balls+1):
        f_b *= i
        
    # 계산
    answer = f_b / (f_b_s * f_s)
    return answer