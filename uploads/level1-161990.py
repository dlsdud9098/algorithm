def solution(wallpaper):
    answer = []

    min_width = len(wallpaper[0])
    max_width = 0
    max_height = 0
    min_height = len(wallpaper)


    for idx_i,paper in enumerate(wallpaper):
        # 가로 최대값 찾기
        for idx_j, p in enumerate(reversed(paper)):
            if p == '#':
                max_width = max(max_width, len(paper) - idx_j)
                min_width = min(min_width, len(paper) - idx_j - 1)

        # 세로 최대값 찾기
        if '#' in paper:
            max_height = max(max_height, idx_i+1)
            min_height = min(min_height, idx_i)
    
    answer = [min_height, min_width, max_height, max_width]
    return answer