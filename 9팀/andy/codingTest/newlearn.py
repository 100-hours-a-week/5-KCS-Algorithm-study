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

arr = [5, 1, 1, 1, 2]
print(findMinGeneration(arr))