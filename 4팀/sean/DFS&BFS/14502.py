from collections import deque

import sys

def bfs():
    global max_safe
    q = deque()
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]