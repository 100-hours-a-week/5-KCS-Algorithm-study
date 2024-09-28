import sys
from collections import deque

input = sys.stdin.readline


def binary_search(n):
    head = 0
    tail = len(arr) - 1
    exist = False

    while head <= tail:
        mid = (head + tail) // 2

        if arr[mid] < n:
            head = mid + 1

        elif arr[mid] > n:
            tail = mid - 1

        else:
            exist = True
            return exist
        # 아에 없는 경우도 생각.
    return exist


n = int(input())

arr = list((map(int, input().split())))

arr.sort()

m = int(input())

arr2 = list(map(int, input().split()))

for i in arr2:
    exist = binary_search(i)
    print(1 if exist else 0, end=' ')