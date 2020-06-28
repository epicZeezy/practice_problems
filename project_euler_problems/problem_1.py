# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

import sys

class Solution(object):

    @staticmethod
    def find_multiples(first_multiple, second_multiple, threshold):
        return sum([multiple for multiple in range(threshold) if multiple % first_multiple == 0 or multiple % second_multiple == 0 ])


def main():
    first_multiple = int(sys.argv[1])
    second_multiple = int(sys.argv[2])
    threshold = int(sys.argv[3])
    solution = Solution.find_multiples(first_multiple, second_multiple, threshold)
    print(solution)


main()
