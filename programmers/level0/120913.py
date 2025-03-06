def solution(my_str, n):
    list_a = []
    
    for i in range(0, len(my_str), n):
        list_a.append(my_str[i:i+n])
    return list_a