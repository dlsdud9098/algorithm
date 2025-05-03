"""
1. 숫자가 존재하고 같은 자리에 있으면 strike
2. 숫자가 존재하지만 같은 자리에 없으면 Ball
3. 존재하는 숫자는 하나이지만 입력을 2개를 했다면 Ball 1개
    computer = 010, predict = 101 => [2B]
    존재하는 숫자와 입력되는 숫자의 개수가 맞아야 n Ball 가능 

게임이 끝나고 내가 어떤 숫자를 예측했고 결과과가 어땠는지 기록이 있어야 한다.
"""

import random

def input_num_size():
    while (1):
        num_size = input('맞추실 숫자 자리수를 입력해 주세요')
        if not num_size.isdigit():
            print('숫자가 아닙니다.')
        else:
            num_size = int(num_size)
            break

    return num_size

def check_predict_num():
    while (1):
        predict_num = input("숫자를 입력하세요")
        
        if not predict_num.isdigit():
            print('숫자가 아닙니다.')
        elif len(predict_num) != num_size: 
            print('자리수가 다릅니다. ')
        else:
            predict_num = [i for i in predict_num]

            break
    return predict_num

if __name__ == '__main__':
    records = {}

    # num_size = input_num_size()    

    # # 컴퓨터 랜덤 숫자
    # computer_Bnum = [str(random.randint(0, 9)) for _ in range(num_size)]

    computer_Bnum = ['1', '8', '1']

    num_size = 3
    
    # 맞출 수 있는 횟수
    correct_count = 5
    for i in range(1, correct_count+1):
        results = []
        
        predict_num = check_predict_num()

        """
        따로 찾는 이유는
        만약 랜덤 숫자가 0 8 1 일때
        내가 1 1 1을 예상하면 2b 1s가 나오게 된다.
        그래서 따로 temp를 만들어 기존에 랜덤하게 나온 숫자를 복사하고
        strike를 먼저 찾아 있을 경우에 1s를 부여하고 temp에 있는 숫자를 제거함으로서
        중복을 방지한다.


        """

        temp_Bnum = computer_Bnum.copy()
        # strike 찾기 
        for com_num, pre_num in zip(computer_Bnum, predict_num):
            if com_num == pre_num:
                results.append('Strike')
                temp_Bnum.remove(pre_num)

        print(temp_Bnum)
        
        # Ball 찾기 
        for pre_num in predict_num:
            if pre_num in temp_Bnum:
                results.append('Ball')
            
        if results.count('Strike') == 3:
            print('모두 맞춤')
            break
        print(results)
