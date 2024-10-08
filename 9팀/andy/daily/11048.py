n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for j in range(1, m):
    graph[0][j] = graph[0][j - 1] + graph[0][j]

for i in range(1, n):
    graph[i][0] = graph[i - 1][0] + graph[i][0]


for i in range(1, n):
    for j in range(1, m):
        graph[i][j] = max(graph[i-1][j], graph[i][j-1]) + graph[i][j]

print(graph[n-1][m-1])