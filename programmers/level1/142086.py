def solution(s):
    answer = []
    
    # 임시 문자열
    string = ''
    # 하나씩 뽑기
    for i in s:
        # 임시 문자열에 해당 글자가 없으면
        if not i in string:
            # answer에 -1 넣고 임시 문자열에 글자 추가
            answer.append(-1)
            string += i
        # 있으면
        else:
            # 뒤에서 부터 해당 글자의 위치를 찾고
            num = string.rfind(i)
            # 마지막 위치와 찾은 위치를 뺀 값을 넣는다.
            answer.append(len(answer)-num)
            string += i
    return answer