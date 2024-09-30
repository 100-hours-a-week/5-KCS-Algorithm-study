import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]


end = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    if end < c:
        end = c
    graph[a].append((b, c))
    graph[b].append((a, c))


def bfs(a, b, w):
    visited = set()
    q = deque()
    q.append(a)
    visited.add(a)
    while q:
        now = q.popleft()
        if now == b:
            return 1
        for next, c in graph[now]:
            if next not in visited and c >= w:
                visited.add(next)
                q.append(next)
    return 0

c, d = map(int, input().split())

start = 1

while start <= end:
    mid = (start + end) // 2
    if bfs(c, d, mid):
        start = mid + 1
    else:
        end = mid - 1
print(end)