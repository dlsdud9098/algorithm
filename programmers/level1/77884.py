def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        nums = []
        for j in range(1, i+1):
            if i % j == 0:
                if not j in nums:
                    nums.append(j)
                else:
                    break
                
        if len(nums) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer