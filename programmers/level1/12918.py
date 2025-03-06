def solution(s):
    answer = True
    
    # 글자수 확인
    if len(s) == 4 or len(s) == 6:
        # 영어 있는지 확인
        for w in s:
            if w.isalpha():
                answer = False
    else:
        answer = False
    
    return answer