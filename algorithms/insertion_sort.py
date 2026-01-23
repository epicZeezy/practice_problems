

def insertion_sort(arr):
    for i in range(1, len(arr)):
        number_to_find_position_for = arr[i]
        cursor_index = i - 1
        current_index = i
        while cursor_index >= 0 and arr[cursor_index] > number_to_find_position_for:
            import pdb; pdb.set_trace()
            arr[cursor_index], arr[current_index] = arr[current_index], arr[cursor_index]
            current_index = cursor_index
            cursor_index -= 1
    return arr



assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3 ,4, 5]