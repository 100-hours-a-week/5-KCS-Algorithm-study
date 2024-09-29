import sys
from collections import deque
input = sys.stdin.readline

# n 나라의 개수 m 항로의 개수
n, m = map(int, input().split())

# 나라가 사용하는 언어의 번호
lan = list(map(int, input().split()))
# m개의 줄 각 항로가 연결하는 두 나라의 번호
graph = [[0] for _ in range(n+1)]

for i in range(m):
    country1, country2 = map(int, input().split())
    if not country2 in graph[country1]:
        graph[country1].append(country2)
        graph[country2].append(country1)

def bfs(k):
    q = deque()
    q.append((1, lan[0]))  # 나라, 언어
    visited = [False] * (n+1)  # 방문한 나라
    visited[1] = True # 1번 나라 방문처리
    cnt = 1

    while q:
        country, language = q.popleft()
        for next_country in graph[country]:
            if next_country == 0:
                continue

            if (lan[next_country-1] == language or lan[next_country-1] == k or lan[next_country-1] == lan[0]) and not visited[next_country]:
                q.append((next_country, lan[next_country - 1]))
                visited[next_country] = True
                cnt += 1
    return cnt

result = 0

for k in range(1, 11):
    result = max(result, bfs(k))

print(result)


