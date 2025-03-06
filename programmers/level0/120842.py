def solution(num_list, n):
    answer = [[]]
    num_list.insert(0,'')
    k = 0
    num = []
    for i in range(1, len(num_list)):
        num.append(num_list[i])
        if i % n == 0:
            answer.append(num)
            num = []
            k += 1
    answer = answer[1:]
    return answer