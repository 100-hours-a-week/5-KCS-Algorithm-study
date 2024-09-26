n, m = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

# print(arr)
dp = [[0] * m for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(m):
        if i == 1:
            dp[i][j] = arr[i -1][j]
        else:
            if (arr[i-1][j]):
                if j-1 >=0:
                    dp[i][j] += dp[i-1][j-1]
                dp[i][j] += dp[i-1][j]
                if j + 1 < m:
                    dp[i][j] += dp[i-1][j+1]
            dp[i][j] = dp[i][j] % 1000000007

print(sum(dp[-1]) % 1000000007)
        