def solution(x):
    answer = True
    
    nums = []
    for i in range(len(str(x))):
        nums.append(int(str(x)[i]))
        
    if x % sum(nums) == 0:
        answer = True
    else:
        answer = False
    return answer