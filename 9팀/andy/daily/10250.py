t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    a = n % h
    b = (n - 1) // h
    if a == 0:
        a = h
    b += 1
    if len(str(b)) == 1:
        print(str(a) + "0" + str(b))
    else:
        print(str(a) + str(b))