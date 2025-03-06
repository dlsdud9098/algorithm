import random
def solution(babbling):
    bab = ['aya', 'ye', 'woo', 'ma']
    
    cnt = 0
    for bb in babbling:
        num = len(bb)
        for b in bab:
            if b in bb:
                num -= len(b)
                        
        if num == 0:
            cnt += 1
                
    return cnt