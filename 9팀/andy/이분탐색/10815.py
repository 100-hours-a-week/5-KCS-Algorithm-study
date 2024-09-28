n = int(input())
a = set()
narr = list(map(int, input().split()))
for el in narr:
    a.add(el)
m = int(input())
barr = list(map(int, input().split()))

for el in barr:
    if el in a:
        print(1, end = " ")
    else:
        print(0, end = " ")
