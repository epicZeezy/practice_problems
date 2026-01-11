'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
Examples:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''
from typing import List

def set_zeroes(matrix: List[List[int]]) -> List[List[int]]:
    # Find current zero indexes. Iterate through entire Matrix
    # If 0 and not in visited, get neighbors and do the update. Add indexes to visited to discount
    # Need to do this without extra space. So not as easy
    # Can break loop
    # neighbors = set()
    row_length = len(matrix)
    column_length = len(matrix[0])
    for row_index in range(row_length):
        row = matrix[row_index]
        column_length = len(row)
        for column_index in range(column_length):
            row_column_value = row[column_index]
            if row_column_value == 0:
                current_column_index = column_index - 1                               
                # Zero out rows
                while current_column_index >= 0:                                                    
                    # neighbors.add((row_index, current_column_index))
                    matrix[row_index][current_column_index] = float("-inf") if matrix[row_index][current_column_index] != 0 else 0               
                    current_column_index -= 1
                current_column_index = column_index + 1                               
                while current_column_index < column_length:                    
                    # neighbors.add((row_index, current_column_index))
                    matrix[row_index][current_column_index] = float("-inf") if matrix[row_index][current_column_index] != 0 else 0  
                    current_column_index += 1
                current_row_index = row_index - 1
                # Zero Out Column
                while current_row_index >= 0:                   
                    # neighbors.add((current_row_index, column_index))
                    matrix[current_row_index][column_index] = float("-inf") if matrix[current_row_index][column_index] != 0 else 0              
                    current_row_index -= 1
                current_row_index = row_index + 1
                while current_row_index < row_length:
                    # neighbors.add((current_row_index, column_index))
                    matrix[current_row_index][column_index] = float("-inf") if matrix[current_row_index][column_index] != 0 else 0
                    current_row_index += 1
    for i in range(row_length):
        for j in range(column_length):
            if matrix[i][j] == float("-inf"):
                matrix[i][j] = 0
    # for row_index, column_index in neighbors:
    #     matrix[row_index][column_index] = 0
    return matrix
'''
[1,1,1]
[1,0,1]
[1,1,1]
'''
matrix_1 = [[1,1,1],[1,0,1],[1,1,1]]
assert set_zeroes(matrix_1) == [[1,0,1],[0,0,0],[1,0,1]]
matrix_2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
assert set_zeroes(matrix_2) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

'''
Understand: Zero out row and column if a value is 0. Like that one game I forget. Blitz something. Or mines
Match: In-place. Seems like a two pointer approach as well here. Need to find zero and then use other pointer to find other row_i, row_j without conflicting with other pointers
Will need to keep track of indexes I'm adding to zero set so we don't duplicate work
Plan
Implement
Review
Evaluate
'''