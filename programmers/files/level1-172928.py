# park, routes, result = ["SOO","OOO","OOO"],	["E 2","S 2","W 1"],	[2,1]
# park, routes, result = ["SOO","OXX","OOO"],	["E 2","S 2","W 1"],	[0,1]
park, routes, result = ["OSO","OOO","OXO","OOO"],	["E 2","S 3","W 1"],	[0,0]

map_height = len(park) - 1
map_width = len(park[0]) - 1

map = {}

dont_go = []

# park에서 시작 지점 찾기 
for i, m in enumerate(park):
    for j, n in enumerate(m):
        map[f'({str(i)}, {str(j)})'] = n
        if n == 'S':
            if_start_h, if_start_w = (i, j)

now_h, now_w = if_start_h, if_start_w

# 현재 위치가 맵을 벗어났는지 확인 
def out_map(height, width, park, map):
    if (height > len(park) - 1) or (height < 0):
        return (1, 'h')
    
    if (width > len(park[0]) - 1) or (width < 0):
        return (1, 'w')
    
    if (map[f'({str(height)}, {str(width)})'] == 'X'):
        return (1, 'X')

    return 0

# 좌표 이동하면서 확인하기
def move(n, op, height, width, ori_height, ori_width):
    for _ in range(n):
        if (op == 'E'):
            width += 1
        elif op == 'S':
            height += 1
        elif op == 'E':
            width -= 1
        elif op == 'N':
            height -= 1

        r = out_map(height, width, park, map)
        if not out_map:
            num, d = r
            if num:
                if d == 'h':
                    height = ori_height
                    break
                elif d == 'w':
                    width = ori_width
                    break
    return (height, width)
            

print(map)
for route in routes:
    op, n = route.split(' ')
    n = int(n)

    # 동쪽일 때 
    if op == 'E':
        now_h, now_w = move(n, op, if_start_h, if_start_w, now_h, now_w)
    elif op == 'N':
        now_h, now_w = move(n, op, if_start_h, if_start_w, now_h, now_w)
    elif op == 'W':
        now_h, now_w = move(n, op, if_start_h, if_start_w, now_h, now_w)
    elif op == 'S':
        now_h, now_w = move(n, op, if_start_h, if_start_w, now_h, now_w)
    # now_h, now_w = if_start_h, if_start_w

print(now_h, now_w, result)

a = [now_h, now_w]
print(a == result)








# def solution(park, routes):
#     answer = []
    
#     map_height = len(park) - 1
#     map_width = len(park[0]) - 1

#     map = {}

#     dont_go = []

#     # park에서 시작 지점 찾기 
#     for i, m in enumerate(park):
#         for j, n in enumerate(m):
#             map[f'({str(i)}, {str(j)})'] = n
#             if n == 'S':
#                 start_h, start_w = (i, j)

#     now_h, now_w, if_start_h, if_start_w = (start_h, start_w)*2



#     print(map)
#     for route in routes:
#         op, n = route.split(' ')
#         n = int(n)

#         # 동쪽일 때 
#         if op == 'E':
#             # 한 칸씩 이동
#             for i in range(1, n+1):
#                 if_start_w += 1
#                 # 현재 위치가 맵을 벗어났다면 원래대로 돌아감 
#                 if (if_start_w > map_width):
#                     if_start_w = now_w
#                     break
#                 # 만약 현재 위치에 장애물이 있으면 원래대로 돌아감 
#                 if (map[f'({str(if_start_h)}, {str(if_start_w)})'] == 'X'):
#                     if_start_w = now_w
#                     break
#         elif op == 'N':
#             for i in range(1, n+1):
#                 if_start_h -= 1
#                 if (if_start_h < 0):
#                     if_start_h = now_h
#                     break
#                 if (map[f'({str(if_start_h)}, {str(if_start_w)})'] == 'X'):
#                     if_start_h = now_h
#                     break
#         elif op == 'W':
#             for i in range(1, n+1):
#                 if_start_w -= 1
#                 if (if_start_w < 0):
#                     if_start_w = now_w
#                     break
#                 if (map[f'({str(if_start_h)}, {str(if_start_w)})'] == 'X'):
#                     if_start_w = now_w
#                     break
#         elif op == 'S':
#             for i in range(1, n+1):
#                 if_start_h += 1
#                 print(f'({str(if_start_h)}, {str(if_start_w)})')
#                 if (if_start_h > map_height):
#                     if_start_h = now_h
#                     break
#                 if (map[f'({str(if_start_h)}, {str(if_start_w)})'] == 'X'):
#                     if_start_h = now_h
#                     break
#         now_h, now_w = if_start_h, if_start_w

#     print(now_h, now_w)


#     answer = [now_h, now_w]
#     return answer
