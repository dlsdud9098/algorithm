def solution(num_list):
    answer = []
    
    if num_list[-1] > num_list[-2]:
        answer.append(num_list[-1] - num_list[-2])
    else:
        answer.append(num_list[-1] * 2)
        
    answer = num_list + answer
    return answer