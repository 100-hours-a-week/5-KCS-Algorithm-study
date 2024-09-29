d, n = map(int, input().split())

oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))
mino = 1e9
for i in range(d):
    # print(oven[i], mino)
    if oven[i] < mino:
        mino = oven[i]
    else:
        oven[i] = mino
end = d
start = 0 
# print(oven)
start = 0
end = d - 1
now = -1
for el in pizza:
    caninit = 0
    temp = end
    if oven[start] < el:
        now = -1
        break
    # print(start, end)
    while start <= end:
        mid = (start + end) // 2
        # print(mid, oven[mid])
        if oven[mid] >= el:
            start = mid + 1
            caninit = 1
        else:
            end = mid - 1
    if caninit == 0:
        now = -1
        break
    # now = end
    start = 0
    end -= 1
    now  = end + 1

print(now + 1)