n, m = map(int, input().split())

arr = []
acu = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        acu[i + 1][j + 1] = acu[i][j + 1] + acu[i + 1][j] - acu[i][j] + arr[i][j]

# print(arr, acu)

for _ in range(m):
    a,b,c,d = map(int, input().split())
    print(acu[c][d] + acu[a - 1][b - 1] - acu[c][b - 1] - acu[a - 1][d])