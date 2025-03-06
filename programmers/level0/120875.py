def solution(dots):
    result = []
    
    # 기울기 계산하고 저장하기
    for idx, i in enumerate(dots):
        for j in dots[idx+1:]:
            x = i[0] - j[0]
            y = i[1] - j[1]
            
            result.append(y / x)
    
    # 같은 기울기의 값이 2개이거나 4개 이상인 경우 return 1 아니면 0
    for i in result:
        if result.count(i) == 2 or result.count(i) > 3:
            return 1
            
    return 0