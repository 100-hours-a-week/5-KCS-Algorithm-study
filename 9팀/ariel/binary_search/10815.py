# 정렬, 이진 탐색
N = int(input())
nums = sorted(list(map(int, input().split())))
M = int(input())
cards = list(map(int, input().split()))
ans = []

for c in cards:
    s = 0
    e = N - 1 # 첨에 N로 둬서 인덱스 에러 남!
    have = 0

    while s <= e:
        mid = (s + e) // 2
        if nums[mid] == c:
            have = 1
            break

        elif nums[mid] < c:
            s = mid + 1
        else:
            e = mid - 1

    ans.append(have)

print(*ans)