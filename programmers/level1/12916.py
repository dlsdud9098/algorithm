def solution(s):
    p_num = 0
    y_num = 0
    for i in range(len(s)):
        if s[i] == 'P' or s[i] == 'p':
            p_num += 1
        if s[i] == 'y' or s[i] == 'Y':
            y_num += 1
        
    if p_num == y_num:
        return True
    else:
        return False