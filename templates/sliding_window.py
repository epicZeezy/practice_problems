def sliding_window(arr):
    left = 0
    current_state = 0
    
    # Use a for loop for the right pointer
    for right in range(len(arr)):
        # 1. Expand: Add the element at the right pointer
        current_state += arr[right]
        
        # 2. Contract: While the condition is broken, move the left pointer
        while condition_is_invalid(current_state):
            current_state -= arr[left]
            left += 1
            
        # 3. Process: Update your result (max length, min sum, etc.)
'''
Comparison
Feature         for loop (Right Pointer)  while loop (Right Pointer)
Complexity      O(n)                      O(n)
Boilerplate     Low (handled by range)   High (needs manual increment)
Best For        Standard expansion       Non-linear movement
Readability     High                     Moderate

'''