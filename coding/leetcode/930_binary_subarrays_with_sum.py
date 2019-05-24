# https://leetcode.com/contest/weekly-contest-108/problems/binary-subarrays-with-sum/

def numSubarraysWithSum(A: List[int], S: int) -> int:
    """
    Number of sub-arrays that have the specified sum.

    Each sub-array contains a contiguous set of values from the original
    list, and can overlap with other sub-arrays.

    Approach:
    Starting from the first index, check successively larger sub-arrays, counting
    each sub-array for which the sum matches the specified value, and jumping to
    the next loop iterertion when the sum exceeds that value.
    ==> THIS IS THE NAIVE IMPLEMENTATION, WHICH IS WILL TIME-OUT DUE TO O[n^n] COMPLEXITY

    An improved approach will use a dictionary to record the index position of all
    in the list, then check for contiguous indices that sum to the target value.
    This must be implemented differently for the case when the target is zero.
    """
    # Create lists to track index location for each number.
    ones = []
    #zeros = []
    for i, item in enumerate(A):
        if int(item) == 1:
            ones.append(i)
        #else:
        #    zeros.append(i)
    # Add a dummy node to the end of each list to facilitate the algorithm
    ones.append(len(A))
    #zeros.append(len(A))

    count = 0

    if S == 0:
        # Count all runs of contiguous zeros
        # Using pointers (lp, rp) to the leftmost and rightmost contiguous zeros
        lp = 0
        while len(A) and lp < len(A):
            # Find the next start of a run of zeros
            while lp < len(A) and A[lp] != 0:
                lp += 1
            # Then find the end of that run of zeros
            rp = lp
            while rp < len(A) and A[rp] == 0:
                rp += 1
            rp -= 1             # need to remove the overshoot

            # Now add all combinations of subarrays
            contiguous_zeros = rp - lp + 1
            while contiguous_zeros:
                count += contiguous_zeros
                contiguous_zeros -= 1

            # Advance the pointers
            lp = rp + 1

    else:
        # Count runs of contiguous ones and zeros that sum to S
        # For ones, we are using the list of indices
        previous_one = -1
        for lower_one, upper_one, next_one in zip(ones, ones[S-1:], ones[S:]):
            left_zeros = right_zeros = 0

            if lower_one > previous_one:
                left_zeros = lower_one - previous_one - 1

            if upper_one < len(A):
                right_zeros = next_one - upper_one - 1

            previous_one = lower_one

            # Number of sub arrays associated with this group is one
            # more than the number of zeros on either side.
            count += (left_zeros + 1) * (right_zeros + 1)

    return count
