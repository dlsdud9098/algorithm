'''
n: 택배 개수
w: 가로 개수
num: 꺼내려는 상자 개수
'''
def create_stack():

    storage = []
    # 가로 개수만큼 스택 만들기
    for i in range(w):
        storage.append([i+1])

    now_num = 1               # 현재 숫자 
    prev_flag = 0       # 역으로 넣기
    storage_num = 0     # 현재 넣으려는 스택 위치 


    if n % w != 0:
        stack_num = n // w + 1
    else:
        stack_num = n // w
    # print('stack_num: ', stack_num)

    # 스택 만들 때 이미 1,2,3,4,5 ...는 넣었기 떄문에 1번 안해도 된다 
    for _ in range(stack_num-1):
        # 역방향 
        if prev_flag == 1:
            # 11 9 7 5 3 1 으로 진행 
            for i in range(2*w-1, 0, -2):
                
                # 시작이 6이기 때문에 -1을 먼저 한다
                storage_num -= 1
                
                now_num = (i) + storage[storage_num][-1]
                # 넣어야 하는 값이 택배 개수를 초과하면 넣지 않고 넘기기 
                if now_num > n:
                    continue

                storage[storage_num].append(now_num)

        # 정방향
        else:
            # 1 3 5 7 9 11 으로 진행
            for i in range(1, 2*w, 2):
                now_num = (2*w - i) + storage[storage_num][-1]
                # print(2*w - i, storage[storage_num][-1], now_num)
                
                # 넣어야 하는 값이 택배 개수를 초과하면 넣지 않고 넘기기 
                if now_num > n:
                    storage_num += 1
                    continue
        
                storage[storage_num].append(now_num)

                storage_num += 1

        # 정방향으로 다 넣으면 역방향으로 바꾸기 
        if prev_flag == 1:
            prev_flag = 0
        else:
            prev_flag = 1

        # 택배 개수보다 초과되면 멈추기 
        if now_num > n:
            break
            

    # print(storage)

    
    for i in range(len(storage)):
        try:
            num_index = storage[i].index(num)
            stack_num = i
        except:
            pass

    print(f'n: {n}, w: {w}, num: {num}')
    print(len(storage[stack_num]) - 1)

if __name__ == '__main__':
    n = 13
    w = 3
    num = 6

    # 몇 번째 라인인지는 모르지만 행이 1번째에 있음을 알 수 있음 
    # 6 12 18과 같이 딱 떨어지는 숫자여도 같은 행에 있으니 미리 -1
    row_line = (num - 1) // w
    print(row_line, '행')

    # 전체 행의 수
    rows = n // w
    if n % w != 0:
        rows += 1

    
    print(f'현재 위치: {row_line}행에 위치해 있고 그 행의 수는 {rows}칸')

    # 열 위치 찾기
    # 정방향 (왼 -> 오), 1 3 5 7 9 ...
    if row_line % 2 == 0: 
        column = (num - 1) % w
    # 역방향 (오 -> 왼), 11 9 7 5 ....
    else:
        column = w - (num - 1) % w - 1

    if w * column > n:
        rows -= 1
        
    storage = []
    
    for r in range(1, rows):
        # 짝수 행 
        if r % 2 == 0:
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
            current_num = r * w + column + 1
        else:
            '''
            2행 이기 때문에 해당 행의 최대값은 2*열의 최대값 
            (r + 1) * w ==> 2 * 6 == > 12
            홀수 행은 오른쪽에서 왼쪽으로 숫자가 커지기 때문에 왼쪽에 있는 숫자가 가장 큼
            오른쪽으로 갈 수록 숫자가 줄어들기 때문에 열의 수(4)만큼 작아짐 
            '''
            current_num = (r + 1) * w - column
        storage.append(current_num)

    print(storage)

    print(len(storage) - storage.index(num))