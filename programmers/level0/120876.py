def solution(lines):
    answer = {}
    line_n = {}
    line1 = []    
    values = []
    cnt = 0

    # 한 곳으로 모으기
    for i in range(lines[0][0], lines[0][1]+1):
        line1.append(i)
    
    # 1칸 씩 나누기
    for idx, line in enumerate(lines):
        line_n[idx] = [[i, i+1] for i in range(line[0], line[1])]
        
    # 2차원으로 만들기
    for i in line_n.values():
        for j in i:
            values.append(j)
                
    # 개수 세기
    for i in values:
        if not str(i) in answer:
            answer[str(i)] = 1
        else:
            answer[str(i)] += 1
            
    for i in answer.values():
        if i >= 2:
            cnt += 1
    return cnt