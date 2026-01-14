def merge(left_arr, right_arr):
    if len(left_arr) == 0:
        return right_arr
    if len(right_arr) == 0:
        return left_arr
    if left_arr[0] < right_arr[0]:
        return [left_arr[0]] + merge(left_arr[1:], right_arr)
    if right_arr[0] < left_arr[0]:
        return [right_arr[0]] + merge(left_arr, right_arr[1:])

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr)//2
    left_arr = mergeSort(arr[:middle])
    right_arr = mergeSort(arr[middle:])
    return merge(left_arr, right_arr)

arr = [38, 27, 43, 10]
assert mergeSort(arr) == [10, 27, 38, 43]
print(arr)