import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

st = []
for i in range(n):
    st.append(int(input()))

st.sort(reverse=True)

result = -1

for i in range(n - 2):
    if st[i] < st[i + 1] + st[i + 2]:
        result = st[i] + st[i + 1] + st[i + 2]
        break

print(result)