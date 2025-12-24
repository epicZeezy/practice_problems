def isIsomorphic(s: str, t: str) -> bool:
        new_string = ""
        existing_mapping = {}
        values_mapping = {}
        for index, s_char in enumerate(s):
            t_char = t[index]
            if s_char in existing_mapping:
                new_string += existing_mapping[s_char]
            elif t_char in values_mapping and s_char not in existing_mapping:
                return False
            else:
                new_string += t_char
                existing_mapping[s_char] = t_char
                values_mapping[t_char] = s_char
        if new_string == t:
            return True
        return False
assert isIsomorphic("baba", "badc") == False
assert isIsomorphic("egg", "add") == True
'''
Understand: Can chars in s be replaced to make t. Is this as easy as it's the same length? What's an example where they're the same length and don't match
abba dank
daad
Match: Hash table to map characters make sense
Plan/Pseudocode:
    - Could map index of each character to the other and map
    - egg vs add. Well it needs to map or it'll be wrong. e need to map to a
Implement
Reflect
Evaluate
'''