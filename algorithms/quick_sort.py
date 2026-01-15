# partition function
def partition(arr, low, high):
    
    # choose the pivot
    pivot = arr[high]
    
    # index of smaller element and indicates 
    # the right position of pivot found so far
    i = low - 1
    
    # traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for k in range(low, high):
        if arr[k] < pivot:
            i += 1
            swap(arr, i, k)
    
    # move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1

# swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# the QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        print(arr)
        
        # recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


numbers_to_sort = [3, 1, 7, 2, -1, 10]
n = len(numbers_to_sort)
quickSort(numbers_to_sort, 0, n - 1)
assert numbers_to_sort == [-1, 1 , 2, 3, 7, 10]


#  [3, 1, 7, 2, -1, 10] pivot = 2, start = 3, end = 10
# [2, 1, 7, 3, -1, 10]  leftArr = [2, 1, 7], start = 2, end = 7
# [1, 2, 7, 3, -1, 10]   