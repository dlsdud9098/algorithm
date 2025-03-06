def solution(sides):
    answer = 0
    
    # 주어진 변에 가장 긴 변이 있을 때
    # 가장 긴 변 <= 나머지 두 변의 합
    # 나머지 한 변 <= 가장 긴 변
    # 나머지 한 변이 가장 긴 변일 때
    # 주어진 선 중 가장 긴 변 < 가장 긴 변 < 주어진 두 변의 합
    
    # 주어진 선에 가장 긴 선이 있을 때
    max_side = max(sides)
    min_side = min(sides)
    other_side = []
    for i in range(1, max_side+1):
        if max(sides) < i + min(sides):
            if i <= max(sides):
                other_side.append(i)
    
    # 나머지 한 선이 가장 긴 선일 때
    for i in range(max(sides)+1, sum(sides)):
        if max(sides) < i < sum(sides):
            other_side.append(i)
    print(other_side, len(other_side))
    answer = len(other_side)
    return answer