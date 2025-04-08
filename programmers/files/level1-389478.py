def solution(n, w, num):
    answer = 0
    
    # 가로의 길이와 딱 맞아 떨어지는 숫자 (6, 12, 18)가 있기 때문에 -1 해준다.
    rows = (num - 1) // w

    # 행의 최대 길이
    row_line = n // w + 1 if n % w else n // w

    # 열 찾기
    if rows % 2 == 0:
        col = (num - 1) % w
    else:
        col = (w -(num - 1) % w) - 1

    stacks = []
    for row in range(row_line):
        # 행이 짝수인 경우
        if row % 2 == 0:
            '''
            현재 행의 값 
            현재 행 : r => 0
            전체 열의 수: w = > 짝수수이기 때문에 0 2 4 6...
            해당 숫자가 있는 열 위치: column => 0 1 2 3 4 5 <= w-1

            값이 1부터 시작하기 때문에 +1

            ex) 2행인 경우
            r(2행) * w(총 6개의 열) + column(4열) + 1
            2행이기 때문에 최대 열(6) 의 2배인 12부터 시작
            12로부터 열(4)만큼 더한 곳에 위치해 있음
            숫자는 1부터 시작하기 때문에 마지막에 +1

            ==> 2행 4열 ==> 17
            '''
            curr_num = row * w + col + 1
            stacks.append(curr_num)
        # 행이 홀수인 경우
        else:
            '''
            2행 이기 때문에 해당 행의 최대값은 2*열의 최대값 
            (r + 1) * w ==> 2 * 6 == > 12
            홀수 행은 오른쪽에서 왼쪽으로 숫자가 커지기 때문에 왼쪽에 있는 숫자가 가장 큼
            오른쪽으로 갈 수록 숫자가 줄어들기 때문에 열의 수(4)만큼 작아짐 
            '''
            curr_num = (row + 1) * w - col
            stacks.append(curr_num)

        # 만약 최대 숫자를 넘어서면 하나 뺌
        if curr_num > n:
            stacks.pop()        
            break

    answer = len(stacks) - stacks.index(num)

    return answer