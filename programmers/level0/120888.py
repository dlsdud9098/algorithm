def solution(my_string):
    split_string = []
    string_list = []
    answer_list = []
    for i in range(len(my_string)):
        split_string.append(my_string[i])
        
    for i in range(len(split_string)):
        if not split_string[i] in string_list:
            string_list.append(split_string[i])
            answer_list.append(split_string[i])
        
    return ''.join(answer_list)