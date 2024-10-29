def minDeletions(arr):
    n = len(arr)

    li = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:  # 증가하는 부분인지 확인
                li[i] = max(li[i], li[j] + 1)  # 갱신

    max_lis_length = max(li)

    if (n - max_lis_length) == 0:
        return n - max_lis_length
    else:
        return n - max_lis_length - 1

arr = [6, 7, 5, 4, 3]
print(minDeletions(arr))

# def minDeletions(arr):
#     n = len(arr)
#     inversions = 0  # 역전 횟수 초기화
#
#     for i in range(n - 1):
#         if arr[i] > arr[i + 1]:
#             inversions += 1  # 역전 발생 시 카운트 증가
#
#     # 최소 삭제 횟수는 역전 횟수에서 1을 뺀 값과 0 중 큰 값
#     min_deletions = max(0, inversions - 1)
#
#     return min_deletions
#
# # 테스트 케이스
# print(minDeletions([3, 4, 2, 5, 1]))  # 출력: 1
# print(minDeletions([1, 2, 3, 4, 5]))  # 출력: 0
# print(minDeletions([5, 4, 3, 2, 1]))  # 출력: 3
# print(minDeletions([2, 1, 7]))        # 출력: 0
# print(minDeletions([4, 2, 1]))        # 출력: 2