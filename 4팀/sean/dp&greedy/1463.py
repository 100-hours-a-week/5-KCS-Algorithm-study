import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

def bfs(n):
    q = deque()
    q.append((n, 0))
    visited = [False] * (n+1)
    visited[n] = True
    result = []

    while q:
        now, cnt = q.popleft()
        if now == 1:
            result.append(cnt)
        for next in (now / 3, now / 2, now - 1):
            if next == int(next) and not visited[int(next)]:
                visited[int(next)] = True
                q.append((next, (cnt+1)))
            else:
                continue
    return result

ans = bfs(n)
print(min(ans))
