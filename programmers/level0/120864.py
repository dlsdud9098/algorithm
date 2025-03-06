def solution(my_string):
    answer = 0
    for i in range(len(my_string)):
        if my_string[i].isalpha():
            my_string = my_string.replace(my_string[i], ' ')
            
    my_string = my_string.split(' ')
    
    result = ' '.join(my_string).split()
        
    for i in result:
        answer += int(i)
    return answer