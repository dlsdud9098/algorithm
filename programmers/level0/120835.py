def solution(emergency):
    answer = []
    # 순서를 담을 딕셔너리
    emer_dict = {}
    # 원래 순서
    real_emer = sorted(emergency, reverse = True)
    # 순서대로 딕셔너리에 담는다.
    for idx, i in enumerate(real_emer):
        emer_dict[i] = idx
    
    # 기존의 emergency의 순서대로 뽑아 진짜 순서를 부여한다.
    for idx, i in enumerate(emergency):
        answer.append(emer_dict[i]+1)
    return answer
