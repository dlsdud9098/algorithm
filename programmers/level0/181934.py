def solution(ineq, eq, n, m):
    answer = 0
    
    case = {
        '>!': n > m,
        '<!': n < m,
        '>=': n >= m,
        '<=': n <= m
    }
    
    if case[ineq+eq] == True:
        answer = 1

    return answer