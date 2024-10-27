def indexSort(arr, indices):
    arr.sort(key = lambda x: tuple((-x[index] if direction == 1 else x[index] for index, direction in indices)))

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    k = int(input())
    indices = []
    for _ in range(k):
        indices.append(list(map(int, input().split())))
    indexSort(arr, indices)

    for row in arr:
        print(' '.join(map(str, row)))