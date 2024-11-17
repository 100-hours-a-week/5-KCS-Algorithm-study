import sys

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    print(N, K)

    arr = list(map(int, input().split()))
    new_arr = set()
    arr_tuple = tuple(arr)
    new_arr.add(arr_tuple)

    steps = 0
    MAX_STEPS = 10000
    result = -1

    while steps < MAX_STEPS:
        if all([x == arr[0] for x in arr]):
            result = steps
            break

        steps += 1
        arr.append(arr[K - 1])
        arr.pop(0)

        arr_tuple = tuple(arr)
        if arr_tuple in new_arr:
            result = -1
            break
        else:
            new_arr.add(arr_tuple)
    print("#%d %d" % (test_case, result))
