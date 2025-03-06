def solution(my_string, num1, num2):
    one = my_string[num1]
    two = my_string[num2]
    
    switch_list = []
    for i in range(len(my_string)):
        switch_list.append(my_string[i])
    
    switch_list[num1] = two
    switch_list[num2] = one
    
    switch_list = ''.join(switch_list)
    return switch_list
