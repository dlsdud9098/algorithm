def solution(n):
    answer = []
    
    for i in range(len(str(n))):
        answer.append(str(n)[i])
    answer = sorted(answer, reverse=True)
    return int(''.join(answer))