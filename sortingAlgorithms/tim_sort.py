import math

def insertion_sort(data, left=0, right=None):
    if right is None:
        right = len(data) - 1

    for index in range(left + 1, right + 1):
        current_value = data[index]
        position = index

        while position > left and data[position - 1] > current_value:
            data[position] = data[position - 1]
            position -= 1

        data[position] = current_value


def merge(data, left, mid, right):
    left_copy = data[left:mid + 1]
    right_copy = data[mid + 1:right + 1]

    l_idx, r_idx = 0, 0
    sorted_idx = left

    while l_idx < len(left_copy) and r_idx < len(right_copy):
        if left_copy[l_idx] <= right_copy[r_idx]:
            data[sorted_idx] = left_copy[l_idx]
            l_idx += 1
        else:
            data[sorted_idx] = right_copy[r_idx]
            r_idx += 1

        sorted_idx += 1

    while l_idx < len(left_copy):
        data[sorted_idx] = left_copy[l_idx]
        l_idx += 1
        sorted_idx += 1

    while r_idx < len(right_copy):
        data[sorted_idx] = right_copy[r_idx]
        r_idx += 1
        sorted_idx += 1


def tim_sort(data):
    min_run = 32
    n = len(data)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(data, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(data, left, mid, right)

        size *= 2
