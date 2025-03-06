def solution(my_string):
    answer = 0
    for i in range(len(my_string)):
        try:
            a = int(my_string[i])
            
            answer += a
        except:
            pass
    return answer
