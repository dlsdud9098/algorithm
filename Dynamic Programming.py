# monoization 방식
def fibonacci_memoization(n, memo=None):
    # 처음에 값을 저장할 dict을 만듦
    if memo is None:
        memo = {}
    # 만약 특정 계산식의 값이 존재한다면
    if n in memo:
        # 그 값을 가져와 리턴시킴
        return memo[n]
    # 만약 계산하려고 하는 값이 1일 경우에
    if n <= 1:
        # 1 리턴
        return n
    # 만약 계산된 값이 없고 새롭게 게산해야 하는 경우 계산하여 새로 집어넣음
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

# 테스트
n = 10
print(f"F({n}) =", fibonacci_memoization(n))

# bottom up 방식
def fibonacci_bottom_up(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 테스트
n = 10
print(f"F({n}) =", fibonacci_bottom_up(n))
