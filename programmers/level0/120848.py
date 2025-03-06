def solution(n):
    answer = 1
    fac = {}
    for i in range(1,11):
        fac_val = 1
        for j in range(1, i+1):
            fac_val *= j
        # print(fac_val)
        fac[fac_val] = j
        
    for i, j in sorted(fac.items(), reverse=True):
        if i <= n:
            return j