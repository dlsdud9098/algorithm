def solution(s):
    cnt_dict = {}
    for i in range(len(s)):
        if s[i] in cnt_dict:
            cnt_dict[s[i]] += 1
        else:
            cnt_dict[s[i]] = 1
            
    one_s_list = []
    
    for i, j in cnt_dict.items():
        if j == 1:
            one_s_list.append(i)
    
    one_s_list = sorted(one_s_list)
    one_s = ''.join(one_s_list)
    return one_s