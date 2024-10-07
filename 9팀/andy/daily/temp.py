import sys
input = sys.stdin.readline

# 3 15
# 1
# 5
# 12
# 3

# n 동전의 종류 개수, k 도달해야하는 금액

# 사용한 동전의 개수의 최솟값(종류 상관 x) => DP
# 불가능하면 -1


n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()
dp = [0] * (k+1)
dp[0] = -1

"""
종류\dp  0   1   2   3   4   5   6   7   8   9   10   11   12   13   14   15
1       0   1   2   3   4   0   1   2   3   4   0    1    0    1    2    0

5       0   0   0   0   0   1   1   1   1   1   2    2    0    0    0    3

12      0   0   0   0   0   0   0   0   0   0   0    0    1    1    1    0

        -1  1   2   3   4   1   2   3   4   5   2    3    1    2    3    3

먼저 동전의 종류를 sort 오름차순
가장 작은 동전부터 시작해서 쌓아가고 
다음 동전만큼 카운트 감소시키는걸로 가자
"""
cnt = 0
for i in range(1, k+1): # 0 ~ 15 까지 순회
    for j in range(n): # coin 순회
        if i < coins[0]: # 불가능한 경우
            dp[i] = -1

        elif i >= coins[j] and i % coins[j] == 0:
            dp[i] = i // coins[j]

        elif i >= coins[j] and i % coins[j] != 0: # 이후값
            dp[i] = min(dp[i], (i // coins[j]) + dp[i - (coins[j]*(i//coins[j]))])

for i in range(len(dp)):
    if dp[i] == 0:
        dp[i] = -1

print(dp[k])