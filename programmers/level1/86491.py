def solution(sizes):
    answer = 0
    max_width = 0
    max_height = 0
    
    for size in sizes:
        max_width = max(max(size), max_width)
        max_height = max(min(size), max_height)

    answer = max_width * max_height
    return answer