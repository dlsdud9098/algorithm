def solution(array, commands):
    answer = []
    
    # commands 하나씩 빼기
    for command in commands:
        # 자른 배열을 담을 임시 배열
        arr = []
        # 배열 자르기
        arr = array[command[0]-1:command[1]]
        # 배열 정렬하기
        arr.sort()
        # 자리수 뽑기
        answer.append(arr[command[2]-1])
    return answer