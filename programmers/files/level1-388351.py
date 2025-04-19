if __name__ == '__main__':
    schedules = [730, 855, 700, 720]
    timelogs = [[710, 700, 650, 735, 700, 931, 912], 
                [908, 901, 805, 815, 800, 831, 835], 
                [705, 701, 702, 705, 710, 710, 711], 
                [707, 731, 859, 913, 934, 931, 905]]
    startday = 1
    answer = 0
    

    # print((i + startday - 1) % 7)
    for schedule, timelog in zip(schedules, timelogs):
        if not timelog:
            continue
        if schedule > 1100 and schedule < 700:
            continue
        if startday <1  and startday > 7:
            continue
        
        # print(timelog)
        for i, log in enumerate(timelog):
            if (i + startday - 1) % 7 + 1 not in {6, 7}:
                if not log <= schedule + 10:
                    continue
        answer += 1
        
        # print(timelog)
        # timelog = [log for i, log in enumerate(timelog) if (i + startday - 1) % 7 + 1 not in {6, 7}]
        
        # # print(timelog)
        
        # if timelog and all(log <= schedule + 10 for log in timelog):
        #     answer += 1
        
    print(answer)