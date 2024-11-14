import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def bfs():
    q = deque()
    q.append((0, 0, 1))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    cnt = 0

    while q:
        x, y, cnt = q.popleft()

        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))


print(bfs())