def solution(nums):
    answer = 0

    # 각 폰켓몬의 종류의 갯수
    one_list = set(nums)
    # 뽑아야 하는 수가 종류의 갯수보다 많거나 같으면
    if len(nums) // 2 <= len(one_list):
        answer = len(nums) // 2
    # 뽑아야 하는 수가 종류의 갯수보다 적으면
    else:
        answer = len(one_list)
    return answer