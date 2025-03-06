def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        try:
            a = int(my_string[i])
            answer.append(a)
        except:
            pass
            
    return sorted(answer)