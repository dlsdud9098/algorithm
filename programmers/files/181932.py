def solution(code):
    answer = ''
    mode = 0
    
    for idx, s in enumerate(code):
        # mode가 1일 경우
        if mode == 1:
            # 현재 문자가 '1'인 경우
            if s == '1':
                mode = 0
            # 현재 문자가 '1'이 아닌 경우
            else:
                if idx % 2 == 1:
                    answer += s
        # mode가 0일 경우
        else:
            # 현재 문자가 '1'인 경우
            if s == '1':
                mode = 1
            # 현재 문자가 '1'이 아닌경우
            else:
                if idx % 2 == 0:
                    answer += s
                
            
    if answer == '':
        return 'EMPTY'
    return answer