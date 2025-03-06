def solution(price, money, count):
    answer = -1
    
    sum = 0
    # 총 금액
    for i in range(1, count+1):
        sum += price * i
    
    # 필요한 금색 계산
    answer = sum - money
    if answer <= 0:
        return 0
    else:
        return answer''