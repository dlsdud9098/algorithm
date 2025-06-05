def solution(number):
    answer = 0
    
    # 처음부터 끝까지(0)
    for idx1, n1 in enumerate(number):
        # 두 번째부터 끝까지(1)
        for idx2, n2 in enumerate(number[idx1+1:]):                
            # 세 번째부터 끝까지(2)
            for idx3, n3 in enumerate(number[idx2+2+idx1:]):
                if n1 + n2 + n3 == 0:
                    answer += 1
    return answer