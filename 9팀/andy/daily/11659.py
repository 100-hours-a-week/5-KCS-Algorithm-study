n, m = map(int, input().split())

arr = list(map(int, input().split()))

acu = [0] * (n + 1)

for i in range(1, n + 1):
    acu[i] = acu[i -1] + arr[i - 1]

for _ in range(m): 
    a, b = map(int, input().split())
    print(acu[b] - acu[a - 1])
    # print(acu)