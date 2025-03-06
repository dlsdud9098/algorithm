def solution(absolutes, signs):
    sum = 0
    for num, sign in zip(absolutes, signs):
        if sign == False:
            num *= -1
        sum += num
    
    return sum