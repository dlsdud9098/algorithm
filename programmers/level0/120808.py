def solution(numer1, denom1, numer2, denom2):
    answer = []
    # 분모가 다를때
    if denom1 != denom2:
        num1 = numer1 * denom2
        den1 = denom1 * denom2
        num2 = numer2 * denom1
        den2 = denom2 * denom1
    
        sum_num = num1 + num2
        sum_den = denom1 * denom2
    # 분모가 같을 때
    else:
        sum_num = numer1 + numer2
        sum_den = denom1
    
    # 분자와 분모가 같을 때
    if sum_num == sum_den:
        answer = [1,1]
    # 다를 때
    else:
        for i in range(2, max(sum_num, sum_den)):
            # 나눌 수 있으면 나누기
            if (sum_num % i == 0) and (sum_den % i == 0):
                sum_num = sum_num // i
                sum_den = sum_den // i

        answer = [sum_num, sum_den]
    return answer