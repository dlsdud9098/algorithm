def solution(s, n):
    answer = ''
    
    for char in s:
        # 대문자일때
        if char.isupper():
            num = ord(char) + n
            # Z를 넘어가면 A로 돌아감
            if num > 90:
                num -= 26
            answer += chr(num)
            pass
        # 소문자일때
        elif char.islower():
            num = ord(char) + n
            # z를 넘어가면 a로 돌아감
            if num > 122:
                num -= 26
            answer += chr(num)
            pass
        # 빈킨일때
        elif char == ' ':
            answer += ' '
            
    return answer