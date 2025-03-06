def solution(dots):
    answer = 0
    
    # 가장 오른쪽 위의 좌표
    line1_max_x = dots[0][0]
    line1_max_y = dots[0][1]
    line1 = 0
    
    # 가장 왼쪽 밑의 좌표
    line2_max_x = dots[0][0]
    line2_max_y = dots[0][1]
    line2 = 0    

    # 좌표 구하기
    for dot in dots:
        if (line1_max_x >= dot[0]) and (line1_max_y >= dot[1]):
            line1_max_x = dot[0]
            line1_max_y = dot[1]
            line1 = dot
        
        if (line2_max_x <= dot[0]) and (line2_max_y <= dot[1]):
            line2_max_x = dot[0]
            line2_max_y = dot[1]
            line2 = dot
        
    
    # 가로와 세로의 길이
    x = line2[0] - line1[0]
    y = line2[1] - line1[1]
    
    answer = x * y
    
    return answer