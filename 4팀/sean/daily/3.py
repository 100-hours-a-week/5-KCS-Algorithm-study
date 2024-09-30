import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

# 가수 인원 수
n = int(input())

# 가수들 영향력
effect = list(map(int, input().split()))

comb = list(combinations(effect, 3))
cnt = 0
for check in comb:
    if not (check[0] > check[1] + check[2] or check[1] > check[0] + check[2] or check[2] > check[0] + check[1]):
        cnt += 1

print(cnt)