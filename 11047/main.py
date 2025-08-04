import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

print(coins)
