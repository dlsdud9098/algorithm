def solution(numlist, n):
    dict = {}
    for num in numlist:
        du = num-n
        if du < 0:
            du *= -1
        if du in dict.keys():
            dict[du].append(num)
        else:
            dict[du] = [num]
            
    aa = []
    for i in sorted(dict.keys()):
        if len(dict[i]) > 1:
            p = sorted(dict[i], reverse=True)
            aa.append(p)
        else:
            print(dict[i])
            aa.append(dict[i])
        
    result = []
    for i in aa:
        result.extend(i)
        
    return result