def solution(box, n):
    answer = 0
    x = box[0]
    z = box[1]
    y = box[2]
    
    num_x = x // n
    num_z = z // n
    num_y = y // n
    
    
    return num_x*num_z*num_y