def solution(order):
    cnt = 0
    for i in range(len(str(order))):
        
        if ('3' == str(order)[i]) or ('6' == str(order)[i]) or ('9' == str(order)[i]):
            cnt += 1
    return cnt