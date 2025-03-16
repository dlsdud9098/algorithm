def solution(a, d, included):
    answer = 0
    
    # a에서부터 공차가 d인 등차수열의 끝 값
    end = (a + d * len(included)) - d
    
    for idx, i in enumerate(range(a, end+1, d)):
        if included[idx] == True:
            answer += i
    return answer