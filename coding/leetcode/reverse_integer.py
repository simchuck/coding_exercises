# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        """
        Given a 32-bit signed integer, reverse the digits
        """
        # Trap the trivial case.
        if x == 0: return 0

        # Store the sign of the original number as a unit value.
        sign = int(x / abs(x))
        x = sign * x

        ## First attempt, pop last digit onto a new list then reassemble.
        #result = []
        #while x:
        #    result.append(str(x%10))
        #    x //= 10
        #reversed_x = int(''.join(result))

        # Or convert to a string, reverse the string, then convert back.
        reversed_x = int(str(x)[::-1])

        ## Another try, this time keeping everything as an integer.
        #reversed_x = 0
        #order = -1
        #
        #x1, x2 = x, x
        #
        #while x1:
        #    order += 1
        #    x1 //= 10
        #
        #while x2:
        #    digit = x2 % 10
        #    reversed_x += digit * (10**order)
        #    order -= 1
        #    x2 //= 10

        # Check for overflow condition on the problem.
        if reversed_x > 2**31: return 0

        # Return with appropriate sign.
        return sign * reversed_x

# Submission Detail
# 1032 / 1032 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Memory Usage: 13 MB
