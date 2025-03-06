def solution(polynomial):
    answer = ''
    
    nums = polynomial.split(' + ')
    sum_x = 0
    sum_num = 0
    for idx, i in enumerate(nums):
        if not i.isnumeric():
            if i[:-1] == '':
                sum_x += 1
            else:
                sum_x += int(i[:-1])
        else:
            sum_num += int(i)
            
    if sum_x == 1:
        if sum_num == 0:
            answer = 'x'
        else:
            answer = f'x + {sum_num}'
    elif sum_x > 1:
        if sum_num == 0:
            answer = f'{sum_x}x'
        else:
            answer = f'{sum_x}x + {sum_num}'
    elif sum_x == 0:
        if sum_num == 0:
            answer = ''
        else:
            answer = f'{sum_num}'
    return answer