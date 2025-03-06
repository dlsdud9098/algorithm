def solution(n):
    cnt = 0
    
    for i in range(1, n+1):
        answer = []
        if i == 1:
            pass
        else:
            for j in range(1, i+1):
                if j in answer:
                    break
                if i % j == 0:
                    answer.append(j)
                    
            if len(answer) >= 3:
                cnt += 1
            
    return cnt