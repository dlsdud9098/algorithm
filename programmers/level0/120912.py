def solution(array):#
    cnt = 0
    for i in range(len(array)):
        array_one = str(array[i])
        for j in range(len(array_one)):
            if array_one[j] == '7':
                cnt += 1
    return cnt##