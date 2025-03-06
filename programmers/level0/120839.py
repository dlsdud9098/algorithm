def solution(rsp):
    answer = []
    for i in range(len(rsp)):
        if rsp[i] == '2':
            answer.append('0')
        elif rsp[i] == '0':
            answer.append('5')
        else:
            answer.append('2')
    return ''.join(answer)