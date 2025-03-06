def solution(arr1, arr2):
    answer = []
    
    # 큰 [] 개수까지
    for i in range(len(arr1)):
        # 임시로 담아둘 배열
        nums = []
        # []안의 원소 숫자만큼
        for j in range(len(arr1[i])):
            nums.append(arr1[i][j] + arr2[i][j])
        answer.append(nums)
    return answer