def solution(board):
    answer = 0
    
    pos = []
    for idr, row in enumerate(board):
        for idc, col in enumerate(row):
            if col == 1:
                pos.append([idr, idc])
                
    cnt = 0
    for i in board:
        for j in i:
            if j == 1:
                cnt += 1
    if cnt == len(board)**2:
        return 0
    
    print(pos)
    for po in pos:
        x = po[0]
        y = po[1]
        
        # print(x, y)
        if y == len(board[0])-1:  
            # 오른쪽 위
            if x == 0 and y == len(board[0])-1:
                board[x+1][y] = 1
                board[x][y-1] = 1
                board[x+1][y-1] = 1
            # 오른쪽 끝
            elif x < len(board[0])-1 and x > -1 and y == len(board[0])-1:
                # 왼쪽 아래
                board[x+1][y-1] = 1
                # 
                board[x-1][y-1] = 1
                # 왼쪽
                board[x][y-1] = 1
                # 아래
                board[x+1][y] = 1
                board[x-1][y] = 1
            elif x == len(board[0])-1:
                board[x-1][y] = 1
                board[x-1][y-1] = 1
                board[x][y-1] = 1
        elif 0 < y < len(board[0])-1:
            # 맨 위
            if x == 0:
                board[x][y+1] = 1
                board[x][y-1] = 1
                board[x+1][y+1] = 1
                board[x+1][y] = 1
                board[x+1][y-1] = 1
            # 맨 아래
            elif x == len(board[0])-1:
                board[x][y-1] = 1
                board[x][y+1] = 1
                board[x-1][y-1] = 1
                board[x-1][y+1] = 1
                board[x-1][y] = 1
            elif x > 0 and x < len(board[0])-1:
                board[x+1][y] = 1
                board[x-1][y] = 1
                board[x][y+1] = 1
                board[x][y-1] = 1
                board[x+1][y+1] = 1
                board[x-1][y-1] = 1
                board[x-1][y+1] = 1
                board[x+1][y-1] = 1
        elif y == 0:
            # 왼쪽
            if x > 0 and x < len(board[0])-1:
                board[x+1][y] = 1
                board[x-1][y] = 1
                board[x+1][y+1] = 1
                board[x-1][y+1] = 1
                board[x][y+1] = 1
            # 왼쪽 아래
            elif x == len(board[0])-1:
                board[x-1][y] = 1
                board[x][y+1] = 1
                board[x-1][y+1] = 1
            elif x == 0:
                board[x+1][y+1] = 1
                board[x+1][y] = 1
                board[x][y+1] = 1
        
    cnt = 0
    for bo in board:
        cnt += bo.count(1)
        
    return len(board)**2 - cnt