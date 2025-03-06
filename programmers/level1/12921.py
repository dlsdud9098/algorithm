def solution(n):
    answer = 0     
            
    # 0부터 n까지의 숫자에 대해 소수인지 여부를 담은 리스트를 초기화 한다.
    sieve = [True] * (n+1) 
    sieve[0], sieve[1] = False, False  # 0과 1은 소수가 아니므로 False 처리한다.

    # 2부터 n의 제곱근까지의 숫자에 대해 반복문을 돌며 소수를 찾는다.
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:  # i가 소수인 경우
            for j in range(i+i, n+1, i):  # i의 배수들을 False로 바꿈
                sieve[j] = False

    # True인 숫자들이 소수이므로, True의 개수를 반환한다.
    answer = sieve.count(True)
    
    return answer