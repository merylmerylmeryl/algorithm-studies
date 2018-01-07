def insertionSort(data):

    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j] < data[j-1]:
            data[j], data[j-1] = data[j-1], data[j]
            j -= 1
