import math
def solution(n):
    a = math.sqrt(n)
    if a == int(a):
        return 1
    else:
        return 2