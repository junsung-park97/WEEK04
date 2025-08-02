import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
item = []
# 물건들 정보 저장
weights = [0]  # 1-based 인덱스를 위해 0 추가
values = [0]


for i in range(n):
    w, v = map(int, input().rstrip().split())
    weights.append(w)
    values.append(v)
    
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for w in range(k + 1):
        # i번째 물건을 선택하지 않는 경우
        dp[i][w] = dp[i-1][w]
        
        # i번째 물건을 선택하는 경우 (무게 제한 확인)
        # dp[i - 1][w - weights[i]] -> 이해가 잘 안감
        if weights[i] <= w:
            dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i]] + values[i])

print(dp[n][k])

