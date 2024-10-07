n = int(input())
m = int(input())

graph = []
parent = [0]
for i in range(1, n + 1):
    parent.append(i)

def find(a):
    temp = a
    while True:
        if parent[a] == a:
            break
        a = parent[a]
    parent[temp] = a
    return a

def union(a,b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pb] = pa

def check(a):
    lena = (len(a))
    pa = find(a[0])
    for i in range(1, lena):
        if pa != find(parent[i]):
            print("NO")
            return
    print("YES")

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i, n):
        if graph[i][j] == 1:
            union(i + 1, j + 1)

arr = list(map(int, input().split()))
check(arr)
