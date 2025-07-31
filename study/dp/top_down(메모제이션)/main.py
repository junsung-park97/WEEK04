# 피보나치 - 재귀 + 메모
# 큰 문제로 시작하여 작은문제로 쪼개기

memo = {}

def fib(n):
    if n in memo:  # 이미 계산했으면
        return memo[n]  # 저장된 값 반환
    
    if n <= 1:
        return n
    
    memo[n] = fib(n-1) + fib(n-2)  # 계산하고 저장
    return memo[n]