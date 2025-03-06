def solution(numbers):
    answer = []
    
    for idx1, i in enumerate(numbers):
        for idx2, j in enumerate(numbers):
            if not idx1 == idx2:
                if not i + j in answer:
                    answer.append(i + j)
    answer.sort()
    return answer