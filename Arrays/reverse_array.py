def reverse_array(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


print(reverse_array([1, 2, 5, 9, 7, 8]))
print(reverse_array([1, 2, 9, 7, 8]))