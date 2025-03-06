def solution(N, stages):
    answer = []
    
    # 스테이지 별 실패율을 구하기 위한 딕셔너리 생성
    lose_stage = {}
    for i in range(1, N+1):
        come_stage = 0  # 해당 스테이지에 도달한 플레이어 수
        lose = 0  # 해당 스테이지를 클리어하지 못한 플레이어 수
        for j in stages:
            # 스테이지에 도달한 플레이어 수 측정
            if j >= i:
                come_stage += 1
            # 스테이지를 클리어하지 못한 플레이어 수 측정
            if i == j:
                lose += 1
                
        # 실패율 계산 후 딕셔너리에 저장
        if lose == 0:
            lose_stage[i] = 0
        else:
            lose_stage[i] = lose / come_stage
    
    # 실패율 기준으로 딕셔너리 정렬 후 answer 리스트에 추가
    lose_stage = sorted(lose_stage.items(), key = lambda x: x[1], reverse = True)
    for i in lose_stage:
        answer.append(i[0])
    
    return answer
