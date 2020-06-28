# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import sys
class Node(object):
    def __init__(self, number, factor_one_node=None, factor_two_node=None):
        self.val = number
        self.factor_one = factor_one_node
        self.factor_two = factor_two_node

    def has_prime_children(self, divisor):
        if self.factor_one and self.factor_two:
            if divisor >= self.factor_one.val and divisor >= self.factor_two.val:
                return True

class Solution(object):

    @staticmethod
    def largest_prime_number(target_num):
        # Start at 2 since everything can be divided by 1 and will need to restart
        # Know we can focus solely on factor one since it's the dividend and factor two can't be greater
        current_factor = Node(target_num, None, None)
        dividend = current_factor.val
        divisor_tally = 2
        current_prime = 1
        while(divisor_tally < dividend and not current_factor.has_prime_children(divisor_tally)):
            quotient = dividend/divisor_tally
            if quotient.is_integer():
                current_factor.factor_one = Node(quotient)
                current_factor.factor_two = Node(divisor_tally)
                dividend = current_factor.factor_one.val
            else:
                divisor_tally += 1

        return current_factor.factor_one.val




def main():
    target_num = int(sys.argv[1])
    largest_prime = Solution.largest_prime_number(target_num)
    print(largest_prime)


main()
