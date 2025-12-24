def minRemoveToMakeValid(s: str) -> str:
        # Get parentheses. If open on stack and we find closing, then we pop it off saying we have a valid one.
        # remaining ones are ones we need to remove. Can keep index for character
        # a)b(c)d
        # Can have separate string for characters added
        # Could also just ignore remaining indexes in stack
        parentheses_stack = []
        full_string = ""
        index_set = set()
        for index, char in enumerate(s):
            if char == "(":
                parentheses_stack.append((char, index))
            if char == ")":
                if parentheses_stack and parentheses_stack[-1][0] == "(":
                    parentheses_stack.pop()
                else:
                    parentheses_stack.append((char, index))
        for item in parentheses_stack:
            index_set.add(item[1])
        for index, char in enumerate(s):
            if index in index_set:
                continue
            full_string += char
        return full_string
assert minRemoveToMakeValid("lee(t(c)o)de)") ==  "lee(t(c)o)de"
assert minRemoveToMakeValid("a)b(c)d") ==  "ab(c)d"
assert minRemoveToMakeValid("))((") == ""
'''
UMPIRE
Understand: Understand the problem. Seems we'd want to remove invalid parentheses? What if we just look at the parentheses and take out the ones not necessary. Keep index for removing/ignore the character. Could do in O(N). Fo
Match: Match the data structure. Stack
Plan: Pseudocode/Plan the code

Implement: Implement the solution
Reflect: Reflect and verify solution. Tests
Evaluate: Time and space complexity

'''