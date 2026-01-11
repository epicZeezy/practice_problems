'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
'''
from typing import List
from collections import defaultdict
def group_anagrams(words: List[str]) -> List[List[str]]:
    # Sort each word
    # Iterate and have sorted word as key that maps to array. Then use all arrays to return answer
    sorted_word_to_anagrams = defaultdict(list)
    all_anagrams = []
    for word in words: # O(N) where N is number of words
        sorted_word = sorted(word)   #O(kLogk)
        sorted_string = "".join(sorted_word) #O(k)
        sorted_word_to_anagrams[sorted_string].append(word)
    
    # Space is O(N)
    for sorted_word, anagrams in sorted_word_to_anagrams.items():
        all_anagrams.append(sorted(anagrams))
    return sorted(all_anagrams)

assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == sorted([["bat"],["nat","tan"],["ate","eat","tea"]])
assert group_anagrams([""]) == sorted([[""]])
assert group_anagrams(["a"]) == sorted([["a"]])

'''
Understand: Anagram is a word that has same characters as another. We're being asked to get the words and group them. Into arrays. One way to do this is to sort each one
Match: Could sort each word, but that'd be nklogk. Could put each word in set and that'd be k if k is number of characters * n. Can we do better. klogk or k. Then multiple by n. kn. I don't think we can do better
Plan: Each word, put into a set so we can check. Another option is a trie. Where we have each word as a trie. No, but order matters there
Implement Done
Review This is what we have but is very inefficient. join. O(Nk) + O(Nklogk)
Evaluate

'''