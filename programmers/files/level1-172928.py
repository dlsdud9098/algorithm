def solution(park, routes):
    answer = []
    
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
            elif op == 'W':
                width -= 1
            elif op == 'N':
                height -= 1

            # 해당 좌표에 문제가 있는지 확인하기
            r = out_map(height, width, park, map)
            if r:
                num, d = r
                # 좌표에 문제가 있으면 기존 좌표로 되돌리기
                if num:
                    if d == 'h':
                        height = ori_height
                        break
                    elif d == 'w':
                        width = ori_width
                        break
                    elif d == 'X':
                        width = ori_width
                        height = ori_height

                        break
            print(height, width)
        return height, width

    for route in routes:
        op, n = route.split(' ')
        n = int(n)

        if op == 'E':
            now_h, now_w = move(n, op, if_start_h, if_start_w, now_h, now_w)
        elif op == 'N':
            now_h, now_w = move(n, op, if_start_h, if_start_w, now_h, now_w)
        elif op == 'W':
            now_h, now_w = move(n, op, if_start_h, if_start_w, now_h, now_w)
        elif op == 'S':
            now_h, now_w = move(n, op, if_start_h, if_start_w, now_h, now_w)

        if_start_h, if_start_w = now_h, now_w



    answer = [now_h, now_w]
    return answer