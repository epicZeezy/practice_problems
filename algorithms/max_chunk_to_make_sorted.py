'''
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.
'''


def merge(arr1, arr2):
    # Check items in arr1 and arr2 and get smallest item and put into resulting array. In this case, if we find the smallest itme on arr1 is bigger
    arr1_pointer = 0
    arr2_pointer = 0
    resulting_chunk = []
    total_chunks = 0
    invalid_chunk = False
    print(arr1, arr2)
    while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):
        if arr1[arr1_pointer] <= arr2[arr2_pointer]:
            resulting_chunk.append(arr1[arr1_pointer])
            arr1_pointer += 1
            if not invalid_chunk:
                total_chunks += 1
        elif arr1[arr1_pointer] > arr2[arr2_pointer]:
            resulting_chunk.append(arr2[arr2_pointer])
            arr2_pointer += 1
            invalid_chunk = True
    if arr1_pointer == len(arr1):
        resulting_chunk.extend(arr2)
    elif arr2_pointer == len(arr2):
        resulting_chunk.extend(arr1)
    return resulting_chunk, total_chunks

def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr, 0
    middle = len(arr) // 2
    left_results, total_left_chunks = merge_sort(arr[:middle]) # Left merge Sort
    right_results, total_right_chunks = merge_sort(arr[middle:])
    resulting_sorted_arr, merged_total_chunks = merge(left_results, right_results)
    total_chunks = total_left_chunks + total_right_chunks + merged_total_chunks
    return (resulting_sorted_arr, total_chunks)



def max_chunks_to_sorted(arr) -> int:
    # maximum_chunks = len(arr)
    # _, total_chunks = merge_sort(arr)
    # print(total_chunks)
    # return maximum_chunks - total_chunks_to_decrement
    # return max(total_chunks, 1)
    stack_chunks = []
    total_chunks = 0
    for item in arr:
        if len(stack_chunks) == 0:
            stack_chunks.append(([item], item))
        else:
            if item < stack_chunks[-1][0][0]:
                stack_chunks[-1][0].append(([item], item))
            elif item >= stack_chunks[-1][1]:
                total_chunks += 1
                stack_chunks.pop()
                stack_chunks.append(([item], item))
    chunks_to_return = total_chunks + len(stack_chunks)
    # print(chunks_to_return)
    # print(stack_chunks)
    return chunks_to_return


# assert merge_sort([4,3,2,1,0]) == ([0, 1, 2, 3, 4], 4)
# Reverse sorted always good example test
assert max_chunks_to_sorted([4,3,2,1,0]) == 1
assert max_chunks_to_sorted([1,0,2,3,4]) == 4
assert max_chunks_to_sorted([1,2,2,3,4]) == 5
assert max_chunks_to_sorted([]) == 0
assert max_chunks_to_sorted([1]) == 1
assert max_chunks_to_sorted([2, 0 ,1]) == 1
'''
UMPIRE
Understand: Need to find largest # chunks to make this array sorted. Sounds like we can't have swapping between chunk. Just the chunk itself is sorted and then see if concatenating/merging would make sorted
Largest number would be they're all their own chunks but that means it's already sorted
Match: Seems sort of similar to merge sort or Quick Sort
Plan: Implement typical merge sort, but instead of swap, just decrement the chunk_size
Implement. Implemented Merge sort from memory despite not yet knowing the swapping operation well. Will have to practice this
Review. Tests pass
Evaluate: Merge Sort time complexity is NLogN. Merge is N.

'''