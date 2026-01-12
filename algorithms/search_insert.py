'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

def search_insert(nums, target) -> int:
    # Get middle element of nums
    # Check if middle is greater or less than target
    # If it is then move start and end to left/right search space instead.
    # Keep doing this till you find the target
    # Will also need to handle what if the target doesn't exist. In this case if start is no longer less than end, we can cancel
    if len(nums) == 1 and nums[0] == target:
        return 0
    if len(nums) == 1:
        index_to_return = 1 if target >= nums[0] else 0
        return index_to_return
    start = 0
    end = len(nums)
    middle_index = None
    while start < end:
        middle_index = (start + end)//2                    # 2
        current_pivot = nums[middle_index]                 # 5
        if current_pivot == target:                        
            return middle_index
        if current_pivot < target:                         
            start = middle_index + 1                       # start = 1
        if current_pivot > target:                         # end = 1, end = 0
            end = middle_index
    # print(middle_index)
    if target > nums[middle_index]:
        return middle_index + 1
    return middle_index


assert search_insert([1, 3, 5, 6], 5) == 2
assert search_insert([1, 3, 5, 6], 2) == 1
assert search_insert([1, 2, 3, 5, 6], 2) == 1
assert search_insert([1], 2) == 1
assert search_insert([1, 3], 2) == 1
assert search_insert([1, 3, 5], 4) == 2


'''
Will likely have to use binary search here.
UMPIRE.
Understand: Need to use binary search here to find target and output index
Match: Binary Search since it's sorted
Plan
Implement
Review
Evaluate

'''