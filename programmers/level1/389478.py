def solution(n, w, num):
    answer = 0
    
    # 가로의 길이와 딱 맞아 떨어지는 숫자 (6, 12, 18)가 있기 때문에 -1 해준다.
    rows = (num - 1) // w

    # 행의 최대 길이
    row_line = n // w + 1 if n % w else n // w

    # 0 ~ 시작
    if rows % 2 == 0:
        col = (num - 1) % w
    else:
        col = (w -(num - 1) % w) - 1

    stacks = []
    for row in range(row_line):
        # 행이 짝수인 경우
        if row % 2 == 0:
            curr_num = row * w + col + 1
            stacks.append(curr_num)
        # 행이 홀수인 경우
        else:
            curr_num = (row + 1) * w - col
            stacks.append(curr_num)

        if curr_num > n:
            stacks.pop()        
            break

    answer = len(stacks) - stacks.index(num)

    return answer