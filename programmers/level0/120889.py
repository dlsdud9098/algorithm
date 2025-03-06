def solution(sides):
    long = max(sides)
    
    long_data = sides.index(long)
    
    sides = sides[:long_data] + sides[long_data+1:]
    if sum(sides) == long:
        return 2
    elif sum(sides) > long:
        return 1
    else:
        return 2