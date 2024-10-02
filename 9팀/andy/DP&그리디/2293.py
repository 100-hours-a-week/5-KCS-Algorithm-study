n, k = map(int, input().split())
arr = [0] * (n)

for i in range(n):
    arr[i] = int(input())


dp = [0] * (k + 1)
dp[0] = 1

for el in arr:
    for i in range(el, k + 1):
        dp[i] += dp[i - el]
print(dp[-1])
