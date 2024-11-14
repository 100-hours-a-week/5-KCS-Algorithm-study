t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    d = y - x
    count = 0
    maxd = 0
    v = 1
    while maxd < d:
        maxd += v
        if count % 2 == 1:
            v += 1
        count += 1
    print(count)