import math
from sortingAlgorithms.quick_sort import quick_sort
from sortingAlgorithms.insertion_sort import insertion_sort

MAX_DEPTH_FACTOR = 2  # Limit recursion depth based on log(size)


def intro_sort(data):
    max_depth = MAX_DEPTH_FACTOR * math.floor(math.log2(len(data)))
    return _intro_sort(data, 0, len(data) - 1, max_depth)


def _intro_sort(data, start, end, max_depth):
    size = end - start + 1

    if size <= 16:  # Use insertion sort for small partitions
        return insertion_sort(data[start:end + 1])

    if max_depth == 0:  # Use heap sort when depth limit is reached
        return heap_sort(data[start:end + 1])

    pivot = partition(data, start, end)
    _intro_sort(data, start, pivot - 1, max_depth - 1)
    _intro_sort(data, pivot + 1, end, max_depth - 1)

    return data


def partition(data, low, high):
    pivot = data[high]
    i = low
    for j in range(low, high):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i], data[high] = data[high], data[i]
    return i


def heap_sort(data):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[largest] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

    return data
