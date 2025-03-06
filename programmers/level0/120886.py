def solution(before, after):
    before_dict = {}
    for i in range(len(before)):
        if not before[i] in before_dict:
            before_dict[before[i]] = 1
        else:
            before_dict[before[i]] += 1
            
    after_dict = {}
    for i in range(len(after)):
        if not after[i] in after_dict:
            after_dict[after[i]] = 1
        else:
            after_dict[after[i]] += 1

    print(before[i])
            
    print(before_dict, after_dict)
    
    if after_dict == before_dict:
        return 1
    else:
        return 0