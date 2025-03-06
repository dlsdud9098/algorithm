def solution(dartResult):
    answer = 0
    
    c = 0  # 각 기회에서 얻은 점수를 저장하는 변수
    sum_list = []  # 총 점수를 계산하기 위해 각 기회에서 얻은 점수를 저장하는 리스트
    for id, i in enumerate(dartResult):
        num_list = len(sum_list)
        
        # 숫자일 때
        if i.isnumeric():
            # 이전 문자도 숫자인 경우 (10점인 경우)
            if dartResult[id-1].isnumeric():
                c = int(dartResult[id-1]+dartResult[id])
            # 일반적인 경우
            else:
                c = int(i)
        # 알파벳일 때
        elif i.isalpha():
            # S, D, T 점수 적용
            if i == 'S':
                c = c ** 1
            elif i == 'D':
                c = c ** 2
            elif i == 'T':
                c = c ** 3
                
            sum_list.append(c)  # 점수 리스트에 추가
            
        # * 기호일 때
        elif i == '*':
            # 첫 번째 기회일 때
            if len(sum_list) == 1:
                sum_list[0] *= 2
            # 두 번째 이상 기회일 때
            else:
                sum_list[num_list-1] *= 2  # 이번 기회 점수 2배
                sum_list[num_list-2] *= 2  # 이전 기회 점수 2배
        
        # # 기호일 때
        elif i == '#':
            # 첫 번째 기회일 때
            if len(sum_list) == 1:
                sum_list[0] *= -1
            # 두 번째 이상 기회일 때
            else:
                sum_list[num_list-1] *= -1  # 이번 기회 점수 음수화
        
    answer = sum(sum_list)  # 총 점수 계산
    return answer
