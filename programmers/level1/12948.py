def solution(phone_number):
    answer = []
    
    for i in range(len(phone_number)):
        if i > len(phone_number)-5:
            answer.append(phone_number[i])
        else:
            answer.append('*')
    return ''.join(answer)