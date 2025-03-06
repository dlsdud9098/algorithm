def solution(food):
    answer = []

    # 음식이 2개일 때
    if len(food) == 2:
        # 1번째 음식의 개수가 1개일 때
        if food[1] < 2:
            return '0'
        # 1번째 음식이 2개 이상일 때
        else:
            # 갯수만큼 반복
            for i in range(food[1]):
                answer.insert(0, str(1))
            # 1번째 음식의 개수가 홀수일때 하나 삭제
            if food[1] % 2 == 1:
                del answer[0]
            # 가운데에 물 추가
            answer.insert(len(answer)//2, '0')
    # 음식의 개수가 3개 이상일 때
    else:
        # 음식을 하나씩 가져옴
        for idx, i in enumerate(food[1:]):
            # 현재 answer의 길이 저장
            num = len(answer)
            # 현재 음식의 갯수만큼 반복
            for j in range(i):
                # 음식이 2개 이상일 때만 실행
                if not i < 2:
                    answer.insert(num//2, str(idx+1))
            # 음식의 갯수가 2개 이상이고 홀수일 때 하나 삭제
            if i > 1 and i % 2 == 1:
                num = len(answer)
                del answer[num//2]

        # 마지막으로 가운데에 물 추가
        num = len(answer)
        answer.insert(num//2, '0')

    return ''.join(answer)