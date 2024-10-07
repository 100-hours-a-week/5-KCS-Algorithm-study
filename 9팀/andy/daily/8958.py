t = int(input())

for _ in range(t):
    st = input()
    arr = []
    lens = len(st)
    if st[0] == "O":
        arr.append(1)
    else:
        arr.append(0)
    for i in range(1, lens):
        if st[i] == "O":
            if arr[-1] == 0:
                arr.append(1)
            else:
                arr.append(arr[-1] + 1)
        else:
            arr.append(0)
    print(sum(arr))