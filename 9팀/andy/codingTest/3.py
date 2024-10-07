def solution(D, T):
    n = len(T)
    glass = 0
    gi = -1
    plastic = 0
    pi = -1
    metal = 0
    mi = -1
    for i in range(n):
        for el in T[i]:
            if el == "G":
                glass += 1
                gi = i
            elif el == "M":
                metal += 1
                mi = i
            elif el == "P":
                plastic += 1
                pi = i
    li = max(gi, pi, mi)
    for i in range(1, li + 1):
        D[i] = D[i - 1] + D[i]
    print(D)
    if pi == -1:
        pt = 0
    else:
        pt = plastic + 2 * D[pi]
    if gi == -1:
        gt = 0
    else:
        gt = glass + 2 * D[gi]
    if mi == -1:
        mt = 0
    else:
        mt = metal + 2 * D[mi]
    print(max(pt, mt, gt))

solution([2,5], ["PGP", "M"])