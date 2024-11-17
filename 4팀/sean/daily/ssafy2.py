
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    max_sum = float('-inf')
    for i in range(N - K + 1):
        sum1 = sum(arr[i:i+K])
        for j in range(i + K, N - K + 1):
            sum2 = sum(arr[j:j+K])
            current_sum = sum1 + sum2
            if current_sum > max_sum:
	            max_sum = current_sum
    print("#%d %d" % (test_case, max_sum))


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    sums = [0] * (N - K + 1)
    current_sum = sum(arr[:K])
    sums[0] = current_sum

    for i in range(1, N - K + 1):
        current_sum = current_sum - arr[i - 1] + arr[i + K - 1]
        sums[i] = current_sum

    max_left = [0] * (N - K + 1)
    max_left[0] = sums[0]
    for i in range(1, N - K + 1):
        max_left[i] = max(max_left[i - 1], sums[i])

    max_right = [0] * (N - K + 1)
    max_right[-1] = sums[-1]
    for i in range(N - K - 1, -1, -1):
        max_right[i] = max(max_right[i + 1], sums[i])

    max_sum = float('-inf')
    for i in range(N - K + 1):
        s1 = sums[i]

        if i + K < N - K + 1:
            s2 = max_right[i + K]
            max_sum = max(max_sum, s1 + s2)
        else:
            break

    if N >= 2 * K:
        result = max_sum
    else:
        result = max(sums)

    print("#%d %d" % (test_case, result))


