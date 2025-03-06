def solution(lottos, win_nums):
    answer = []  # 반환할 결과 리스트
    
    lottos1 = sorted(lottos)  # lottos의 복사본 1
    lottos2 = sorted(lottos)  # lottos의 복사본 2
    win_nums = sorted(win_nums)  # win_nums의 복사본 (오름차순 정렬)
    
    high_rank = 0  # 최고 순위 (0을 모두 맞췄을 때)
    low_rank = 0  # 최저 순위 (0을 모두 틀렸을 때)
    len_0 = lottos.count(0)  # lottos에서 0의 개수
    
    # 각 순위에 해당하는 상금을 매핑하는 딕셔너리
    rank = {
        6:1,
        5:2,
        4:3,
        3:4,
        2:5,
        1:6,
        0:6
    }
    
    # 0을 맞춘 수로 채웠을 때 최고 순위 계산
    for i in range(len_0):
        for j in win_nums:
            if not j in lottos1:
                lottos1[i] = j  # lottos1에서 0인 부분을 win_nums로 대체
                
    for i in lottos1:
        if i in win_nums:
            high_rank += 1  # lottos1에서 맞춘 번호 개수를 세서 최고 순위 계산
            
    num = 1
    # 0을 맞춘 수로 채웠을 때 최저 순위 계산
    for i in range(len_0):
        for j in win_nums:
            if (num in lottos2) or (num in win_nums):
                num += 1  # lottos2와 win_nums에 모두 없는 숫자를 찾음
            else:
                lottos2[i] = num  # lottos2에서 0인 부분을 찾은 숫자로 대체
                
    for i in lottos2:
        if i in win_nums:
            low_rank += 1  # lottos2에서 맞춘 번호 개수를 세서 최저 순위 계산
            
    answer = [rank[high_rank], rank[low_rank]]  # 최고 순위와 최저 순위에 해당하는 상금을 리스트에 담아서 반환
    
    return answer####
