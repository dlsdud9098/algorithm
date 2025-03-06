def solution(my_string):
    answer = []
    eng = ['a', 'e', 'i', 'o', 'u']
    
    for i in range(len(my_string)):
        if not my_string[i] in eng:
            answer.append(my_string[i])
            
    return ''.join(answer)