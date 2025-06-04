def solution(num_list):
    answer = 0
    
    multi = 1
    for num in num_list:
        multi *= num
        
    sqrt = sum(num_list) ** 2
    
    print(multi, sqrt)
    if multi < sqrt: 
        answer = 1 
    else:
        answer = 0
    return answer