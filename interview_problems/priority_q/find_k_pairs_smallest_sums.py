from dataclasses import dataclass
from typing import List, Tuple
import heapq
@dataclass
class ItemPair:
    pair: List[int]
    total: int
    index: Tuple[int, int]

    def __eq__(self, other):
        if self.total == other.total:
            return True
        return False
    
    def __lt__(self, other):
        if self.total < other.total:
            return True
        return False

    def __gt__(self, other):
        if self.total > other.total:
            return True
        return False

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Plan. Keep track of visited sums. Have heap to get minimum sum at a time
        # Re-use the smallest element in the other num. What contributed to smallest sum is probably also smallest number
        # Initialize visited for first numbers
        # Keep going till we have K or we've been through all combinations.
        # Use dictionary for visited
        # Have array to store iterative answer
        # Use heap to keep track of minimum sum
        visited = {(0, 0)}
        k_items = [ItemPair(pair=[nums1[0], nums2[0]], total=nums1[0] + nums2[0], index=(0, 0))]
        answer = []
        heapq.heapify(k_items)
        # While we haven't got to end of K and still have items to pop off from heap, continue
            # Get current min heap item. Check if the next item if less than nums exists and if it's in the visited.
            # Get next nums1 and nums2 and add to heap. Next time we pop off we know we'll get the smallest item and can add to answer
            # Push new combinations into heap through iteration
        while k > 0 and k_items:
            current_min_item = heapq.heappop(k_items)
            nums1_index, nums2_index = current_min_item.index
            answer.append(current_min_item.pair)
            # Check for nums1
            if (nums1_index + 1, nums2_index) not in visited and nums1_index + 1 < len(nums1):
                new_item = ItemPair(
                    pair=[nums1[nums1_index + 1], nums2[nums2_index]],
                    total=nums1[nums1_index + 1] + nums2[nums2_index],
                    index=(nums1_index + 1, nums2_index)
                )
                heapq.heappush(k_items, new_item)
                visited.add(new_item.index)
            # Check for nums2
            if (nums1_index, nums2_index + 1) not in visited and nums2_index + 1 < len(nums2):
                new_item = ItemPair(
                    pair=[nums1[nums1_index], nums2[nums2_index + 1]],
                    total=nums1[nums1_index] + nums2[nums2_index + 1],
                    index=(nums1_index, nums2_index + 1)
                )
                heapq.heappush(k_items, new_item)
                visited.add(new_item.index)
            k -= 1

        return answer

'''
Understand the problem. We want the smallest item each time. Issue is we don't know the number of k.
So for example if k was 4, then we'd have to use more than just the lowest element in the first array. We'd have to begin using what's on the other array too. What if it was 9 and wants every combination.
Match Data Structure. I'm leaning more towards heaps here. Where I store the items in a heap first.
Then I know the max I can have is the number of elements in the other array. Don't need a heap because it's already sorted. Could I just iterate through the elements in order and add sums from nums2. If it's the smallest,then that'll have the smallest sum with everything
Plan
Implement
Review
Evaluate
'''