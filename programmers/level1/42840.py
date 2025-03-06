def solution(answers):
    answer = [] # 정답자 번호를 담을 리스트

    s1 = [1,2,3,4,5] # 수포자 1이 찍는 패턴
    s2 = [2,1,2,3,2,4,2,5] # 수포자 2가 찍는 패턴
    s3 = [3,3,1,1,2,2,4,4,5,5] # 수포자 3이 찍는 패턴

    result = { # 각 수포자가 맞힌 문제 수를 저장할 딕셔너리
        1: 0,
        2: 0,
        3: 0
    }

    for idx, a in enumerate(answers): # enumerate를 이용하여 인덱스와 값을 함께 순회
        if s1[idx % len(s1)] == a: # 수포자 1이 찍은 값과 정답이 같으면
            result[1] += 1 # 수포자 1이 맞힌 문제 수 증가
        if s2[idx % len(s2)] == a: # 수포자 2가 찍은 값과 정답이 같으면
            result[2] += 1 # 수포자 2가 맞힌 문제 수 증가
        if s3[idx % len(s3)] == a: # 수포자 3이 찍은 값과 정답이 같으면
            result[3] += 1 # 수포자 3이 맞힌 문제 수 증가

    max_c = max(result.values()) # 가장 많은 문제를 맞힌 수포자의 문제 수
    for i, j in result.items(): # 각 수포자가 맞힌 문제 수를 순회
        if max_c == j: # 가장 많은 문제를 맞힌 수포자면
            answer.append(i) # 정답자 리스트에 추가

    return answer # 정답자 리스트 반환
