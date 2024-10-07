n = int(input())
line = []
for _ in range(n):
    line.append(int(input()))

line.sort(reverse=True)
for i in range(n - 2):
    # print(i, line[i])
    if line[i] < line[i + 1] + line[i + 2]:
        print(line[i] + line[i + 1] + line[i + 2])
        exit(0)
print(-1)