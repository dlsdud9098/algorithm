def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if len(numbers) == 2:
                return numbers[i]*numbers[i+1]
            else:
                if i != j:
                    answer.append(numbers[i]*numbers[j])
    return max(answer)