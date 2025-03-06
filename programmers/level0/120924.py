def solution(common):
    
    num = len(common)
    a = common[num-1] - common[num-2]
    b = common[num-2] - common[num-3]
    
    if a == b:
        answer = common[num-1] + a
    else:
        
        a = common[num-1] / common[num-2]
        b = common[num-2] / common[num-3]

        if a == b:
            answer = common[num-1] * a
    return answer