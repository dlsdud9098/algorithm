def solution(n, arr1, arr2):
    answer = []
    
    arr_l1 = []
    arr_l2 = []
    # arr1 2진법으로 바꾸기
    for arr in arr1:
        two_num = []
        while True:
            if arr == 0:
                break
            else:
                two_num.insert(0, str(arr % 2))
                arr = arr // 2
        if len(two_num) < n:
            for i in range(n-len(two_num)):
                two_num.insert(0, '0')
        arr_l1.append(''.join(two_num))
        
    # arr2 2진법으로 바꾸기
    for arr in arr2:
        two_num = []
        while True:
            if arr == 0:
                break
            else:
                two_num.insert(0, str(arr % 2))
                arr = arr // 2
        if len(two_num) < n:
            for i in range(n-len(two_num)):
                two_num.insert(0, '0')
        arr_l2.append(''.join(two_num))
        
    # 2진법으로 바꾼 arr1, arr2 #, ' '으로 바꾸기
    for arr1, arr2 in zip(arr_l1, arr_l2):
        result = []
        for i, j in zip(arr1, arr2):
            if i == j == '0':
                result.append(' ')
            else:
                result.append('#')
                
        answer.append(''.join(result))
    return answer