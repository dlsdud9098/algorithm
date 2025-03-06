def solution(price):
    answer = 0
    if price < 100000:
        return price
    elif 300000 > price >= 100000:
        return int(price * 0.95)
    elif 500000 > price >= 300000:
        return price * 0.9
    elif price >= 500000:
        return int(price * 0.8)