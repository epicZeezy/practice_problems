# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import sys

class Solution(object):

    @staticmethod
    def largest_palindrome_product(palindrome):
        # n squared and not performant
        product = 0
        max_palindrome = 0
        for i in range(palindrome):
            for j in range(palindrome):
                product = j * i
                product_str = str(product)
                if product_str == product_str[::-1]:
                    if product > max_palindrome:
                        max_palindrome = product
        return max_palindrome

def main():
    palindrome = int(sys.argv[1])
    largest_palindrome_product = Solution.largest_palindrome_product(palindrome)
    print(largest_palindrome_product)


main()
