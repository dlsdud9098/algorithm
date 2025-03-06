def solution(s):
    answer = ''
    
    i = 0
    for w in s:
        if w == ' ':
            i = 0
            answer += ' '
        else:
            if i % 2 == 0:
                answer += w.upper()
                i += 1
            else:
                answer += w.lower()
                i += 1
    return answer