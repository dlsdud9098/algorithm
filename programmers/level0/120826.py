def solution(my_string, letter):
    answer = []
    for i in range(len(my_string)):
        if not my_string[i] == letter:
            answer.append(my_string[i])
    #    
    return ''.join(answer)
