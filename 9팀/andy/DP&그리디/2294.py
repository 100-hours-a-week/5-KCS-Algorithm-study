n, k = map(int, input().split())
arr = [0] * (n)

for i in range(n):
    arr[i] = int(input())


dp = [1e9] * (k + 1)
dp[0] = 0

for el in arr:
    for i in range(el, k + 1):
        dp[i] = min(dp[i - el] + 1, dp[i])
val = dp[-1]
if val == 1e9:
    print(-1)
else:
    print(dp[-1])
