import sys
from collections import deque
input = sys.stdin.readline

def checked_weight(mid):
    q = deque()
    q.append(fac1)
    visited = [False] * (n + 1)
    visited[fac1] = True

    while q:
        now = q.popleft()

        if now == fac2:
            return 1

        for next, w in graph[now]:
            if not visited[next] and (w >= mid):
                q.append(next)
                visited[next] = True
    return 0

# n 섬, m 다리의 정보 개수
n, m = map(int, input().split())

# 다리 정보
graph = [[] for _ in range(n+1)]
# 무게 정보
weight = []

for i in range(m):
    # a 섬, b 섬, C다리 정보
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    weight.append(c)

fac1, fac2 = map(int, input().split())

head = 1
tail = max(weight)

while head <= tail:
    mid = (head + tail) // 2
    if checked_weight(mid): # mid 가능하다면
        head = mid + 1
    else:
        tail = mid - 1

print(tail)


