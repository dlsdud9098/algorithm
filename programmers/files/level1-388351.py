def solution(schedules, timelogs, startday):
    answer = 0

    schedules = [(schedule - 50) + 100 if (schedule + 10) % 100 >= 60 else schedule + 10 for schedule in schedules ]

    for idx, timelog in enumerate(timelogs):
        for day, log in enumerate(timelog):
            # 현재 날짜 계산
            now_day = day+startday
            if now_day > 7:
                now_day -= 7

            if (now_day != 7) and (now_day != 6):
                # 출근 시간보다 일찍 오거나 정상 시간에 왔을 때
                print(log, schedules[idx])
                if log <= schedules[idx]:
                    login = True
                else:
                    login = False
                    break
        
        if login:
            answer += 1
    
    return answer