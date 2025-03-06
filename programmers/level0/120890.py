def solution(array, n):
    min = n**2
    for i in range(len(array)):
        num = array[i] - n
        if num < 0:
            num *= -1
            
        if num < min:
            min = num
            near = array[i]
        elif num == min:
            if array[i] < near:
                near = array[i]
        
    return near