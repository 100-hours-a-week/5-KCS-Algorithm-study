def findMinGeneration(layer):
    max_neurons = max(layer)
    needs = [max_neurons - l for l in layer]

    oddsum = 0
    evensum = 0
    minodd = 0

    for el in needs:
        if el % 2 == 0:
            evensum += el // 2
        else:
            minodd += 1
            oddsum += el

    while oddsum > evensum:
        if oddsum - 2 < minodd:
            break
        oddsum -= 2
        evensum += 1
    while oddsum < evensum:
        oddsum += 2
        evensum -= 1
        # print(needs, oddsum, evensum)
    evensum = max(evensum, oddsum - 1)

    return oddsum + evensum

if __name__ == '__main__':
    print(findMinGeneration([5, 1, 1, 1, 1, 2]))  # 출력: 6
    print(findMinGeneration([4, 2, 2, 3, 5]))  # 출력: 8
    print(findMinGeneration([3, 3, 3, 6]))  # 출력: 2
    print(findMinGeneration([1, 1, 1]))  # 출력: 0
    print(findMinGeneration([3, 4, 2, 5, 1]))  # 출력: 6