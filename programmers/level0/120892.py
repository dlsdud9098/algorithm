def solution(cipher, code):
    code_list = []
    for i in range(1, len(cipher)+1):
        if i % code == 0:
            code_list.append(cipher[i-1])
    return ''.join(code_list)