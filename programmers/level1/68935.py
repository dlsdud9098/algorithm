def solution(n):
    answer = 0
    result=''
    # 3진법으로 바꾸기
    while n:
        result += str(n % 3)
        n = n // 3
        
    # 10진법으로 바꾸기
    answer = int(result, 3)
    return answer