def solution(i, j, k):
    cnt = 0
    for a in range(i, j+1):
        for s in range(len(str(a))):
            if str(k) in str(a)[s]:
                cnt += 1
    return cnt