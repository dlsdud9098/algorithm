def solution(k, m, score):
    answer = 0
    
    # score 리스트를 내림차순으로 정렬합니다.
    score = sorted(score, reverse = True)
    
    # 상자에 들어갈 사과 개수가 m개인 경우에만 이익을 계산할 수 있으므로
    # score 리스트를 m개씩 쪼개서 각각의 상자를 만들어줍니다.
    sum_list = []
    for i in range(0,len(score),m):
        apple_box = score[i:i+m]
        
        # 상자 안에 들어있는 사과 개수가 m개보다 적은 경우는 이익 계산에서 제외합니다.
        if len(apple_box) < m:
            continue
        
        # 한 상자에 들어있는 사과 중 가장 낮은 점수인 p를 찾아서
        # 이 상자의 이익을 계산해줍니다. (p * m)
        one_box = min(apple_box) * m 
        sum_list.append(one_box)
    
    # 이익이 발생하지 않은 경우에는 0을 반환합니다.
    if len(sum_list) == 0:
        return 0
    
    # 모든 상자의 이익을 더해서 최종적인 이익을 계산합니다.
    answer = sum(sum_list)
    return answer
