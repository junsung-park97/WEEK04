# 피보나치 - 반복문
# 작은 문제로 시작하여 큰 문제로 확장해 가기

def fib(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # 작은 것부터 차례로
    
    return dp[n]