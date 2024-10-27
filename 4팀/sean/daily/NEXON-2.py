def closestNumbers(numbers):
    # 1. 배열에서 중복 제거 후 오름차순 정렬
    unique_numbers = sorted(set(numbers))

    # 2. 최소 절대 차이 초기화
    min_diff = float('inf')

    # 3. 최소 절대 차이 찾기
    for i in range(len(unique_numbers) - 1):
        diff = unique_numbers[i + 1] - unique_numbers[i]
        if diff < min_diff:
            min_diff = diff

    # 4. 최소 차이를 갖는 모든 쌍 수집
    result = []
    for i in range(len(unique_numbers) - 1):
        if unique_numbers[i + 1] - unique_numbers[i] == min_diff:
            result.append((unique_numbers[i], unique_numbers[i + 1]))

    # 5. 결과 출력
    for pair in result:
        print(pair[0], pair[1])

# 난 이렇게 제출함
#     numbers.sort()
#
#     min_diff = float('inf')
#
#     for i in range(1, len(numbers)):
#         diff = numbers[i] - numbers[i - 1]
#         min_diff = min(min_diff, diff)
#
#     for i in range(1, len(numbers)):
#         if numbers[i] - numbers[i - 1] == min_diff:
#             print(numbers[i - 1], numbers[i])


if __name__ == "__main__":
    # 샘플 테스트 케이스 0
    print("Sample Output 0:")
    numbers = [4, 2, 1, 3]
    closestNumbers(numbers)

    print("\nsample output 1:")
    numbers = [4, 4, 2, 1, 3]
    closestNumbers(numbers)

    print("\nsample output 2:")
    numbers = [4, 4, -2, -1, 3]
    closestNumbers(numbers)

