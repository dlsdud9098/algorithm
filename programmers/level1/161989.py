n, m, section, result = [8,	4,	[2, 3, 6]	,2]
n, m, section, result = [5,	4,	[1, 3]	,1]
n, m, section, result = [4,	1,	[1, 2, 3, 4]	,4]

maps = [0 if i+1 in section else 1 for i in range(n) ]
print(maps)
answer = 0

flag = True
for s in section:
    start = s-1
    end = len(maps) if start + m > len(maps) else start + m
    print(start, end, s)
    if flag:
        maps[start:end] = [1]*m
        answer += 1
        flag = False
    if not (start < s) and (s < end):
        maps[start:end] = [1]*m
        answer += 1

    print(maps)

print(answer)