'''
Example 1:
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
'''

def find_longest_substring_t(word, t=2):
    # Start and end pointer
    # If length 2 or less, then exit
    # Set to track window duplicates
    # For each window check length of set. If bigger than t/2, then move start index up and index up till end index is equal to length
    if len(word) <= t:
        return len(word)
    start = 0
    end = 2
    max_length = float('-inf')
    # eceba
    while start < end and end <= len(word):                                           # ba
        sub_word = word[start:end]                                      
        tracker = set(sub_word)                                 # {e, b, a}
        if len(tracker) <= 2:
            max_length = max(max_length, len(sub_word))                                          # end = 5
            end += 1
        else:
            start += 1                                               # start = 3
    return max_length


assert find_longest_substring_t("eceba") == 3
assert find_longest_substring_t("ccaabbb") == 5
assert find_longest_substring_t("") == 0
assert find_longest_substring_t("ac") == 2
assert find_longest_substring_t("abcdefgh") == 2
'''
Understand: Need to find subtring with only two unique characters
Match: Two pointer/Sliding window + Set approach. Set Keeps track of characters for each window
Plan
Implement
Review
Evaluate

'''