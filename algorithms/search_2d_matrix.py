'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

'''
from typing import Tuple
def binary_search(numbers, target) -> Tuple[int, bool]:
    start = 0
    end = len(numbers)
    while start < end:
        middle = (start + end) // 2
        pivot = numbers[middle]
        if target < pivot:
            end = middle
        elif target > pivot:
            start = middle + 1
        else:
            return (middle, True)
    if target > numbers[middle]:
        return (middle + 1, False)
    return (middle, False)
    

def search_matrix(matrix, target) -> bool:
    # Binary Search on First Column to find where target is greater than. If it's less than, the first row, then we can ignore that row
    # Then for eligible rows, run binary search on them to find the number
    # if len(matrix[0]) == 
    first_column = [row[0] for row in matrix]
    search_result_pivot, search_result_success = binary_search(first_column, target)
    if search_result_success:
        return search_result_success
    for row_index in range(search_result_pivot):
        current_row = matrix[row_index]
        search_result_pivot, search_result_success = binary_search(current_row, target)
        if search_result_success:
            return True
    return False



assert search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
assert search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False
assert search_matrix([[1,3,5,7]], 7) == True
assert search_matrix([[1, 2]], 1) == True
assert search_matrix([[1], [5]], 5) == True
assert search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 70) == False



'''
UMPIRE
Understand: Row is sorted in ascending order. First column is always sorted. Need to find outi f the target is in the matrix or not. May be able to assume columns are sorted
Match: Binary Search Because we have sorting properties
Plan Done. Using binary search on first column and then using it on entire row
Implement. Done
Review. Tests look good so far
Evaluate

'''