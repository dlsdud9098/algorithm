def solution(s):
    answer = 0

    # 빈칸 별로 나누기
    sum_str = s.split()
    # 더할 숫자만 담을 빈 배열
    sum_list = []
    # 하나씩 뽑기
    for idx, num in enumerate(sum_str):
        # 문자 Z를 발변하면
        if num == 'Z':
            # Z앞의 숫자를 삭제
            sum_list.remove(int(sum_str[idx-1]))
        # 문자 Z가 아니라면
        else:
            # 숫자 추가
            sum_list.append(int(num))
    # 숫자 모두 더하기
    answer = sum(sum_list)
    return answer