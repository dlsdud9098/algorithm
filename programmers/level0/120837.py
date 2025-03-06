def solution(hp):
    answer = 0
    cnt = 0
    while True:
        if hp >= 5:
            hp -= 5
            cnt += 1
        else:
            if hp >= 3:
                hp -= 3
                cnt += 1
            else:
                if hp >= 1:
                    hp -= 1
                    cnt += 1
                else:
                    break
        
    return cnt