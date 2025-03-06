def solution(s1, s2):
    result = []
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                result.append(s1[i])  
    return len(result)