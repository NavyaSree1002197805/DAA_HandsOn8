import random

def partition(array, lower, higher):
    pivot = array[higher]
    i = lower - 1
    for j in range(lower, higher):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[higher] = array[higher], array[i + 1]
    return i + 1

def quickselect(array, lower, higher, i):
    if lower == higher:
        return array[lower]
    pivot_index = partition(array, lower, higher)
    k = pivot_index - lower + 1
    if i == k:
        return array[pivot_index]
    elif i < k:
        return quickselect(array, lower, pivot_index - 1, i)
    else:
        return quickselect(array, pivot_index + 1, higher, i - k)

def ith_order_statistic(array, i):
    if i < 1 or i > len(array):
        return None
    return quickselect(array, 0, len(array) - 1, i)

array = [23,56,77,65,34,54,44,2,3,8]
i = 5
print(f"The {i}th order statistic of {array} is: {ith_order_statistic(array, i)}")

