def solution(A, B):
    cnt = 0
    
    for i in range(len(A)):
        if A == B:
            return cnt
        else:
            cnt += 1
            A = A[len(A) - 1] + A[:-1]
            if A == B:
                return cnt
    
    return -1