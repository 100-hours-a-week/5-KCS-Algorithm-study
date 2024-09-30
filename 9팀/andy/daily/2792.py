n, m = map(int, input().split())
arr = []

for _ in range(m):
    arr.append(int(input()))

end = max(arr)
suma = sum(arr)
start = suma // n

def decide(a):
    count = 0
    for el in arr:
        count += (el // a)
        if el % a:
            count += 1
        # print(a, el, count)
    if count > n:
        return 0
    return 1

while start <= end:
    mid = (start + end) // 2
    # print(mid, decide(mid))
    if decide(mid):
        end = mid - 1
    else:
        start = mid + 1
print(start)