def solution(n):    
    j = 0
    for i in range(1, n+1):
        print(i, j)
        
        # 한 자리수 일 때
        if len(str(j)) == 1:
            j += 1
            # 3과 관련있는 수가 없을 때까지 반복
            while True:
                # 3의 배수거나 3인 숫자가 있으면 +1
                if j % 3 == 0 or str(j) == '3':
                    j += 1
                else:
                    break
        # 두 자리수 일때
        elif len(str(j)) == 2:
            j += 1
            while True:
                # 3의 배수거나 10의 자리가 3이거나 1의 자리가 3이면 +1
                if j % 3 == 0 or str(j)[1] == '3' or str(j)[0] == '3':
                    j += 1
                else:
                    break
        # 세 자리수 일때
        else:
            j += 1
            while True:
                # 3의 배수거나 100의 자리가 3이거나 10의 자리가 3이거나 1의 자리가 3이면 +1
                if j % 3 == 0 or str(j)[0] == '3' or str(j)[1] == '3' or str(j)[2] == '3':
                    j += 1
                else:
                    break
    return j