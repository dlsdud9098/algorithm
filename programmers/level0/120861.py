def solution(keyinput, board):
    answer = []
    
    # 시작 좌표
    result = [0,0]
    
    # 좌표 이동
    for input in keyinput:
        if input == 'up':
            result[1] += 1
        elif input == 'down':
            result[1] -= 1
        elif input == 'left':
            result[0] -= 1
        elif input == 'right':
            result[0] += 1
        
        # 좌표 벗어났을 시
        if abs(result[0]) > board[0]//2:
            if result[0] < 0:
                result[0] += 1
            else:
                result[0] -= 1
        elif abs(result[1]) > board[1]//2:
            if result[1] < 0:
                result[1] += 1
            else:
                result[1] -= 1
        
    return result