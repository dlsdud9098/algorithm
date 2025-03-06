def solution(n):
    answer = 1
    while True:
        if (answer * 6) % n == 0:
            return answer
        answer += 1