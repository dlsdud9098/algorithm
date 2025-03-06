def solution(bin1, bin2):
    bin1_list = []
    sum1 = 0
    for i in range(len(bin1)):
        sum1 += int(bin1[i]) * (2**(len(bin1)-i-1))
        
    bin2_list = []
    sum2 = 0
    for i in range(len(bin2)):
        sum2 += int(bin2[i]) * (2**(len(bin2)-i-1))
        
    sum = sum1 + sum2
    print(sum1 ,sum2, sum)
    plus_list = []
    m = 0
    while True:
        m = int(sum / 2)
        n = sum % 2
        if n == 1:
            plus_list.append('1')
        elif n == 0:
            plus_list.append('0')
        if m == 0:
            break
        sum = m
        print(plus_list)
    answer = []
    for i in range(len(plus_list)-1, -1, -1):
        answer.append(str(plus_list[i]))
    print(answer)
    answer = ''.join(answer)
    return answer