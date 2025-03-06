def solution(n):
    nums = []
    for i in range(1, n+1):
        if n % i == 0:
            if not i in nums:
                nums.append(i)
            else:
                break
                
    return sum(nums)