g = [log for i, log in enumerate(timelog) if (i + startday - 1) % 7 + 1 not in {6, 7}]
        
        # # print(timelog)
        
        # if timelog and all(log <= schedule + 10 for log in timelog):
        #     answer += 1