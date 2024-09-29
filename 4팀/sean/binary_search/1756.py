import sys
from collections import deque
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())

oven = list(map(int, input().split()))

pizza_diameter = list(map(int, input().split()))

# 오븐 재졍렬
for i in range(1, len(oven)):
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]

# 피자가 오븐에 들어간다아
tail = len(oven) - 1
head = 0
piled_loc = 0

for pizza in pizza_diameter:
    is_piled = False

    while head <= tail:
        mid = (head + tail) // 2
        if oven[mid] >= pizza:
            head = mid + 1
            piled_loc = mid
            is_piled = True
        else:
            tail = mid - 1

    if not is_piled:
        piled_loc = -1
        break

    head = 0
    tail = piled_loc - 1

if piled_loc == -1:
    print(0)
else:
    print(piled_loc + 1)