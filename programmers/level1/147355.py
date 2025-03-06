def solution(t, p):
    answer = 0
    
    for j in range(len(t)):
        arr = ''
        if j == len(t)-len(p)+1:
            break
        arr += t[j:j+len(p)]
        if int(p) >= int(arr):
            answer += 1
        
    return answer