import copy

n = int(input())
crain = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crain.sort(reverse=True)
box.sort(reverse=True)

now = [0] * (m)
visited = [0] * m

i = 0
for el in crain:
    while i < m and el < box[i]:
        i += 1
    # print(el, box[i])
    if i < m:
        now[i] = 1
        visited[i] = 1
    i += 1
# print(now)
if now[0] == 0:
    print(-1)
    exit(0)
result = 1
remain = 0
for el in now:
    if el == 0:
        remain += 1
while remain:
    # print(now, remain, result, visited)
    temp = copy.deepcopy(now)
    for i in range(m):
        if now[i] == 1:
            temp[i] = 0
            j = i + 1
            while j < m:
                if visited[j] == 0:
                    temp[j] = 1
                    visited[j] = 1
                    remain -= 1
                    break
                j += 1
    now = temp       
    result += 1
print(result)


