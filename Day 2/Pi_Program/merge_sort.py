import time
import random
import sys

def merge(left, right):

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)

size = int(sys.argv[1])
array = []
for x in range (size):
    array.append(random.randint(1, 1001))
# print(array)
start_time = time.time()
ar = merge_sort(array)
end_time = time.time()
# print(ar)
print(end_time-start_time)
