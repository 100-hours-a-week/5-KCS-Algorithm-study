n, h = map(int, input().split())

top = [0] * (h + 1)
down = [0] * (h + 1)

for i in range(n):
    if i % 2 == 0:
        down[int(input())] = 1
    else:
        top[int(input())] = 1

for i in range(1, h + 1):
    top[i] += top[i - 1]


for i in range()
    down[h - i] += down[h + 1 - i]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
dp = [0] * (h + 1)