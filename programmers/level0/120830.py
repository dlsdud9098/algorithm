def solution(n, k):
    answer = 0
    a = 12000*n
    k -= n//10
    b = 2000*k
    
    answer = a+b
    return answer