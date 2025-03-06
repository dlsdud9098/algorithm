def solution(strings, n):
    answer = []
    
    # key = 어떤 것을 기준으로 할 것인가
    # (x[n], x)는 n번째 글자를 기준으로 오름차순으로 정렬하는 것이고, (x, x[n])는 모든 글자를 기준으로 오름차순으로 정렬
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer