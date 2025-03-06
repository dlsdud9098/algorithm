def solution(n, m):
    answer = []
    
    n1_nums = []
    n2_nums = []
    
    # 최대공약수 구하기
    for i in range(1, n+1):
        if n % i == 0:
            if not i in n1_nums:
                n1_nums.append(i)
                
    for i in range(1, m+1):
        if m % i == 0:
            if not i in n2_nums:
                n2_nums.append(i)
                
    same_nums = []
    for n1 in n1_nums:
        for n2 in n2_nums:
            if n1 == n2:
                same_nums.append(n1)
    
    if len(same_nums) == 1:
        answer.append(1)
    else:
        answer.append(same_nums[-1])
        
    # 최소공배수 구하기
    for i in range(max(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
    return answer