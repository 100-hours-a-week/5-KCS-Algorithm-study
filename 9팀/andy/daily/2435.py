n, k = map(int, input().split())

arr = list(map(int, input().split()))

acu = [0] * (n + 1)

for i in range(1, n + 1):
    acu[i] = acu[i - 1] + arr[i - 1]


result = -1e9
# print(acu)
for i in range(n + 1 - k):
    val = acu[i + k] - acu[i]
    # print(val)
    if val > result:
        result = val

print(result)