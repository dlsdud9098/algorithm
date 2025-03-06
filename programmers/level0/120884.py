def solution(chicken):
    coupon = chicken
    
    eat_chicken = 0
    while True:
        plus_eat = int(coupon / 10)
        eat_chicken += plus_eat
        coupon = plus_eat + coupon % 10
        
        if coupon < 10:
            break
            
    
    return eat_chicken