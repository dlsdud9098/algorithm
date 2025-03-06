def solution(numbers):#
    answer = 0
    for i in numbers:
        for j in numbers:
            if i == j:
                continue
            if i * j > answer:
                answer = i * j
    return answer