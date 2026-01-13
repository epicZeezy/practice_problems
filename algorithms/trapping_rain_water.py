from typing import List
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


'''


def trap(height: List[int]) -> int:
    # How do we know if the water is traped?
    # The left max is higher and the right max is higher:
    current_max = 0
    index_to_max_height = {}
    for index, index_height in enumerate(height):
        if index_height > current_max:
            index_to_max_height[index] = [index_height, None]
            current_max = index_height
        else:
            index_to_max_height[index] = [current_max, None]
    
    current_max = 0
    for i in range(len(height) -1, -1, -1):
        index_height = height[i]
        if index_height > current_max:
            index_to_max_height[i][1] = index_height
            current_max = index_height
        else:
            index_to_max_height[i][1] = current_max
    total_water = 0
    for height_index, left_right_max in index_to_max_height.items():
        current_height = height[height_index]
        water_trapped = min(left_right_max) - current_height
        total_water += water_trapped
    return total_water




assert(trap([2, 0, 0, 0, 2])) == 6
assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert trap([4,2,0,3,2,5]) == 9
assert trap([0,0,0,0]) == 0
assert trap([1,1,1,1]) == 0
assert trap([3,2,1]) == 0
assert trap([1,2,3]) == 0
assert trap([2,0,0, 0, 0, 2]) == 8
assert trap([1]) == 0



'''
UMPIRE
Understand: To trap water. You need a dip in elevation that's smaller than the elevation to the left and right of it. All the same would be 0. Need to find maximum boundary
Match: Tracking left and right max to find out how much water is trapped for each ndex
Plan: Multiple passes
Implement: Done
Review: Looks right based on the test cases here
Evaluate: O(N) space and time complexity. We're passing through the array of heights in multiple phases to get the left and right max here.
Can we do better. Yeah, we can do better because right now we're making multiple passes, but there is a way to potentially have a sliding window keep track
'''