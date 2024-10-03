import sys
from collections import deque
input = sys.stdin.readline

# n 물건 수 , k 가방의 무게
n, k = map(int, input().split())
stuff = [[0, 0]]
#dp
knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]`

for _ in range(n):
    stuff.append(list(map(int, input().split())))

# 냅색 문제 풀이
for i in range(1, n + 1):
    for j in range(1, k + 1): # j 가현재 가방에 남은 무게 용량
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]  # weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[n][k])