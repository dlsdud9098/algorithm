def solution(slice, n):
    if n % slice == 0:
        return n//slice
    elif slice > n:
        return 1
    else:
        return n // slice + 1