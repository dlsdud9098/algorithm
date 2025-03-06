def solution(my_string):
    mystring = my_string.lower()
    
    sort_string = sorted(mystring)
    r_string = ''.join(sort_string)
    
    return r_string