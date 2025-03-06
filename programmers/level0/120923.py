def solution(num, total):
    
    a = total
    while True:
        sum_list = []
        sum = 0
        if a >= 0:
            for i in range(a+1, a+1-num, -1):
                sum += i
                sum_list.append(i)

            if sum == total:
                return sorted(sum_list)
                break
            else:
                a -= 1
        else:
            for i in range(a+num, a, -1):
                sum += i
                sum_list.append(i)
                
            if sum == total:
                return sorted(sum_list)
            else:
                a -= 1
                