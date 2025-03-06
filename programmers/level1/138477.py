def solution(k, score):
    answer = [] # 최종적으로 반환될 리스트
    
    score_rank = [] # 점수를 내림차순으로 정렬한 리스트
    result = [] # 매일 발표되는 명예의 전당의 최하위 점수 리스트
    
    for id, i in enumerate(score): # 각 날짜마다 점수 리스트를 순회
        score_rank.append(i) # score_rank 리스트에 현재 점수를 추가
        score_rank = sorted(score_rank, reverse=True) # score_rank 리스트를 내림차순으로 정렬
        
        if len(score_rank) < k: # 명예의 전당에 k명 미만의 가수가 올라가 있는 경우
            result.append(score_rank[-1]) # 최하위 점수는 현재 score_rank 리스트의 마지막 값
        else: # 명예의 전당에 k명 이상의 가수가 올라가 있는 경우
            result.append(score_rank[k-1]) # 최하위 점수는 score_rank 리스트의 k번째 값
            
    answer = result # 최종적으로 반환될 리스트에 result 리스트 대입
    return answer # 반환
