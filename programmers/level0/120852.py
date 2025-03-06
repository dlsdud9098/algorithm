def solution(n):
    answer = []
    s_n = n
    for i in range(2, n+1):
        # 해당 숫자로 더이상 나눌 수 없을때까지 반복
        while True:
            # 나눌 수 있으면 나누기
            if s_n % i == 0:
                s_n = s_n // i
                # 이미 한 번 이상 나눠본 숫자면 넘어감
                if not i in answer:
                    answer.append(i)
            else:
                break
    return answer