def solution(my_string):
    string_list = []
    for i in range(len(my_string)):
        if my_string[i].isupper():
            string_list.append(my_string[i].lower())
        else:
            string_list.append(my_string[i].upper())
            
    string_list = ''.join(string_list)
    return string_list