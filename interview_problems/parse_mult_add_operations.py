test_cases = [
	("( ADD 1 2 )",3),
	("( ADD 1 ( MULT 2 ( ADD 1 10 ) ) )", 23),
]


# ( ADD 1 ( MULT 2 5 
# ( ADD 1 ( MULT 2 5 



'''
    2
ADD 1

     5
MULT 2
ADD 1
'''

def parse_expression(expression):
	operations_stack = []
	values_stack = []
	for part in expression:
		if part == "ADD" or part == "MULT":
			operations_stack.append(part)
		if part.isdigit():
			values_stack.append(int(part))
	while operations_stack:
		operation = operations_stack.pop()
		first_value = values_stack.pop()
		second_value = values_stack.pop()
		if operation == "ADD":
			current_sum = int(first_value) + int(second_value)
			values_stack.append(current_sum)
		if operation == "MULT":
			current_multiple = int(first_value) * int(second_value)
			values_stack.append(current_multiple)
	return values_stack[-1]

first_expression_split = test_cases[1][0].split()
assert parse_expression(first_expression_split), test_cases[1][1]	
print(parse_expression(first_expression_split))

# O(N) time complexity and O(N) space complexity. Pretty much recursion but using a stack. The parenthesis don't really matter here. We just need to make sure the expressions match with their values

#Understand: Each expression has parenthesis surrounding it. Has MULT/ADD operation and then two values. Values can be an expression. If I can identify an expression then I know I have an operation value value. Base case would be operation value value and values aren't expressions
#D#ata Structure that makes most sense here is a stack
#P#lan: Build a small function to identify an expression and then get operations. We can use a stack for the parenthesis and store start/end. When we have open and closing expression we remove both off and know we have an operation here.
#A#ssumption is that we always will have operation value value no matter what and it'll be wrapped in an expression. So we could do this recursively. This would be O(N) and O(N) time complexity based on what I'm seeing
