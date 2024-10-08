import sys
input = sys.stdin.readline

# n 동전 개수, k 동전의 합
n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

dp = [0 for _ in range(k+1)]

dp[0] = 1
for coin in coins:
    for i in range(k+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]

print(dp[k])

