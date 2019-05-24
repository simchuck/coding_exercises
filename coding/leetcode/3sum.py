# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = list()

        # Sort the list to prepare for the algorithm below
        nums.sort()
        length = len(nums)

        for t in range(0, length-2):

            # No need to check further if all values are same sign
            if nums[t] > 0: break

            # Skip if we already checked same value
            if t > 0 and nums[t] == nums[t-1]: continue

            # Limits are set to remaining indices of nums list
            l, r = t + 1, length -1

            print(f'Entring l<r loop with {t} {l} {r}')
            while l < r:
                total = nums[t] + nums[l] + nums[r]
                if total < 0:
                    # Total value is too low, so increment the lower pointer
                    l += 1
                elif total > 0:
                    # Total value is too high, so decrement the upper pointer
                    r -= 1
                else:
                    # We found one!
                    triplets.append([nums[t], nums[l], nums[r]])
                    # Adjust l,r pointers to avoid repeated values
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1

        return triplets

# Submission Detail
# 313 / 313 test cases passed.
# Status: Accepted
# Runtime: 724 ms
# Memory Usage: 16.7 MB
