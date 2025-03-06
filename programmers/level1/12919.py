def solution(seoul):
    answer = ''
    
    for idx, i in enumerate(seoul):
        if i == 'Kim':
            answer = f'김서방은 {idx}에 있다'
    return answer