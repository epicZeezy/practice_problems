'''
Write a function that takes in an n x m two dimensional array (that can be square-shaped when n == m)
and returns a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeeds in
a spiral pattern all the way until ever element has been visited
'''
# from collections import deque

def get_next_neighbor(node, matrix, visited, direction_idx):
    '''
    Get right, down, left, up in that order and return. If it's visited or out of bounds exclude
    This doesn't work. If you call the right recurisvely each time it'll be wrong. Or maybe should do reverse
    Maybe a DFS
    1, neighbors = [12, 2]
    2, [12, 2, 13, 3]
    circular array for right, down, left, up
    '''
    row_length = len(matrix)
    column_length = len(matrix[0])
    chosen_direction = direction_idx % 4
    right_node = (node[0], node[1] + 1)
    down_node = (node[0] + 1, node[1])
    left_node = (node[0], node[1] - 1)
    up_node = (node[0] - 1, node[1])
    # Go right, down, left, up. If next neighbor is not eligible then return None to signal upstream we finished
    if chosen_direction == 0 and right_node[1] < column_length and right_node not in visited:
        return right_node
    if chosen_direction == 1 and down_node[0] < row_length and down_node not in visited:
        return down_node
    if chosen_direction == 2 and left_node[1] >= 0 and left_node not in visited:
        return left_node
    if chosen_direction == 3 and up_node[0] >= 0 and up_node not in visited:
        return up_node
    return None

def spiral_traverse(array):
    start_node = (0, 0)
    nodes_stack = [start_node]
    row_length = len(array)
    column_length = len(array[0])
    visited = {}
    # Better we don't change the input
    output_array = []
    current_direction = 0
    expected_total = row_length * column_length
    while nodes_stack:
        current_node = nodes_stack.pop()
        nxt_node = current_node
        while nxt_node:
            # import pdb; pdb.set_trace()
            number = array[nxt_node[0]][nxt_node[1]]
            output_array.append(number)
            visited[nxt_node] = True
            nxt_node = get_next_neighbor(nxt_node, array, visited, current_direction)
            if nxt_node is not None:
                current_node = nxt_node
        current_direction += 1
        nxt_node = get_next_neighbor(current_node, array, visited, current_direction)
        if nxt_node is not None:
            nodes_stack.append(nxt_node)
    print(output_array)
    return output_array

    




test_array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]
expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

assert spiral_traverse(test_array) == expected_output


'''
right, down, left, up
1, stack = [12, 2]
2, stack = [12, 13, 14, 3]
3, stack = [12, 13, 14, 4]
4, stack = [12, 13, 14, 5]
5, stack = [12, 13, 14, 16, 6]
'''
