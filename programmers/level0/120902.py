def solution(my_string):
    split_string = my_string.split(' ')
    sum = 0
    for i in range(0, len(split_string)-1, 2):
        if i == 0:
            sum += int(split_string[0])
        
        if split_string[i+1] == '-':
            sum -= int(split_string[i+2])
            continue
        else:
            sum += int(split_string[i+2])
            continue
    return sum
    
    