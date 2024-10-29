def minDeletions(arr):
    # LIS를 찾기 위한 배열
    lis = []

    for num in arr:
        # 이진 탐색을 통해 num이 들어가야 할 위치 찾기
        start, end = 0, len(lis)
        
        while start < end:
            mid = (start + end) // 2
            if lis[mid] < num:
                start = mid + 1
            else:
                end = mid

        # start는 num이 들어가야 할 위치
        if start == len(lis):
            lis.append(num)
        else:
            lis[start] = num

    # 삭제해야 할 원소의 수 = 전체 길이 - LIS의 길이
    return len(arr) - len(lis)

# 예시 사용
arr = [3, 4, 2, 5, 1]
result = minDeletions(arr)
print(result)  # 출력: 1
