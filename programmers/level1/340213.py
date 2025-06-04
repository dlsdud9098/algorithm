def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    # 분-초 -> 초로 바꾸기
    def set_time(t):
        mm, ss = t
        return int(mm) * 60 + int(ss)

    # 모든 시간에 적용
    video_len = set_time(video_len.split(':'))
    pos = set_time(pos.split(':'))
    op_start = set_time(op_start.split(':'))
    op_end = set_time(op_end.split(':'))

    for com in commands:
        # 현재 pos가 op_start와 op_end 사이에 있을 때
        if (op_start <= pos) and (op_end >= pos):
            pos = op_end

        # 명령어가 next일 때 
        if com == 'next':
            pos += 10
            # 영상 길이 벗아닐 시 
            if pos >= video_len: 
                pos = video_len
                continue
        # 명령어가 prev 일 때 
        else:
            pos -= 10
            # 영상 길이 벗어날 시 
            if pos <= 0:
                pos = 0
                continue

    # 초 -> 분-초
    if pos % 60 > 59:
        pos = (pos // 60) + (pos % 60)

    pos = f'{pos // 60:02d}:{pos % 60:02d}'
    
    answer = pos
    return answer