def solution(score):
    rank = 0
    avg = []
    dict = []
    for i in score:
        avg.append(sum(i)/2)
        dict.append([sum(i)/2, 1])
        
    ascend = sorted(avg)
    ascend_dict = []
    cnt = 1
    a = 0
    
    for i in range(len(ascend)-1, -1, -1):
        i += a
        if i < 0:
            break
        elif i == 0:
            ascend_dict.append([ascend[i], cnt])
        else:
            ascend_dict.append([ascend[i], cnt])
            k = 0
            for j in range(i, -1, -1):
                if j == 0:
                    break
                elif ascend[j] == ascend[j-1]:
                    ascend_dict.append([ascend[j-1], cnt])
                    a -= 1
                    k += 1
                else:
                    break
            cnt += k        
        cnt += 1
    
    
    i = 0
    for avg1, rank1 in dict:
        for avg2, rank2 in ascend_dict:
            if avg1 == avg2:
                # print(dict[i])
                
                dict[i][1] = rank2
        i += 1
        
        
    rank = [j for i, j in dict]
    ### print(dict)
    return rank