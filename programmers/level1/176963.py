def solution(name, yearning, photo):
    # answer 리스트 초기화
    answer = []
    
    # 딕셔너리 형태로 이름과 열망도를 매핑
    name_score = {}
    for n, s in zip(name, yearning):
        name_score[n] = s
        
    # yearning 리스트를 name 리스트와 길이를 맞추기 위해 0으로 채움
    append_count = len(name) - len(yearning)
    for i in range(append_count):
        yearning.append(0)
        
    # photo 리스트를 순회하며 각 사진에 대한 점수 계산
    for photos in photo:
        sum = 0
        for p in photos:
            if p in name_score.keys():
                sum += name_score[p]
        answer.append(sum)
    
    return answer