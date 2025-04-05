'''
n: 택배 개수
w: 가로 개수
num: 꺼내려는 상자 개수
'''

if __name__ == '__main__':
    n = 13
    w = 3
    num = 6

    storage = []
    # 가로 개수만큼 스택 만들기
    for i in range(w):
        storage.append([i+1])

    now_num = 1               # 현재 숫자 
    prev_flag = 0       # 역으로 넣기
    storage_num = 0     # 현재 넣으려는 스택 위치 


    if n % w != 0:
        stack_num = n // w + 1
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


    # 몇 번째 라인인지는 모르지만 1번째 칸에 있음을 알 수 있음 
    # print(n // num - 1)
    num_line = n // num - 1

    prev = 0
    start = 1

    if num_line // 2 == 0:
        start = 2*w - 1 + start

        for idx, i in enumerate(range(start, 0, -2)):
            if i == num:
                column = idx
    else:
        start = 1 + start

    # print(column)

    stroage = []
    now_num = 0
    while now_num < n:
        for i in range(stack_num):
            if i // 2 == 0:
                now_num = (2*w - 1) + (i+1)
                print(now_num)
                storage.append(now_num)
            else:
                
                
