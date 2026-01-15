'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

'''

def swap(arr, index_1, index_2):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]

def partition(nums, left, right) -> int:
    # Using right pivot so just assume all elements are smaller
    pivot = nums[right]
    i = left - 1
    for j in range(left, right):
        if nums[j] < pivot:
            i += 1
            swap(nums, i, j)
    
    swap(nums, i + 1, right)
    return i + 1

def quick_sort(nums, left, right):
    if left < right:
        pivot_idx = partition(nums, left, right)
        quick_sort(nums, left, pivot_idx - 1)
        quick_sort(nums, pivot_idx + 1, right)
    return nums

    
if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    assert quick_sort([2,0,2,1,1,0], 0, len(nums) - 1) == [0,0,1,1,2,2]

    assert quick_sort([2,0,1],  0, 2) == [0, 1, 2]


'''

UMPIRE
Understand: Essentially need a sorting in-place algorithm. QuickSort is good for this so we can sort colors
Match: Quick Sort
Plan: Quick Sort Plan. Pick pivot (last item). Then after you pick the pivot, iterate through the arr. Put rest in comments
Implement:
Review:
Evaluate:
'''