# https://leetcode.com/problems/heaters

class Solution:
    def reverse(self, x: int) -> int:
        """
        Given a 32-bit signed integer, reverse the digits
        """
        import sys

        sign = 1
        if x < 0:
            sign = -1
        x *= sign

        # First idea is to do this in decimal, but I suspect it will be
        # relatively expensive in terms of time (and perhaps space).
        #result = []
        #while x:
        #    result.append(x%10)
        #    x //= 10
        #''.join(result)

        # Second idea is to use bit-shifting to construct the reversed
        # number in binary.

        # A third ideas is to convert to a string, reverse the string,
        # then convert back.
        x_reversed = sign * int(''.join(str(x)[::-1]))

        if x_reversed > sys.getsizeof(x): return 0

        return x_reversed


# 536 / 1032 test cases passed.
#     Status: Wrong Answer

