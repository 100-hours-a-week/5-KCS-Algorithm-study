def indexSort(arr, indices):
   arr.sort(key=lambda x: tuple(
        (-x[index] if direction == 1 else x[index]) for index, direction in indices
    ))

arr = [[1, 2, 1], [3, 3, 1], [4, 2, 3], [6, 4, 3]]
indices = [[1, 0], [2, 1]]
indexSort(arr, indices)

print(arr)
