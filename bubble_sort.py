def bubble(array):
    arrayLength = len(array)-1  # minus 1 to avoid list out of range
    sorted = False

    while not sorted:
        sorted = True
        for i in range(arrayLength):
            if array[i] > array[i+1]:
                sorted = False
                array[i], array[i+1] = array[i+1], array[i]
        arrayLength = arrayLength - 1
    return array


array = bubble([5, 1, 8, 10, 7, 3, 6, 9, 2, 4])
print(array)
