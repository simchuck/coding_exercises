"""
Leetcode: 349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.
Each element in the result must be unique.

# https://leetcode.com/articles/intersection-of-two-arrays
"""
from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:

    # Solution 1: Naive approach with nested for loop
    results = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                results.append(nums1[i])
                continue    # we found one, so can skip the rest of this loop
    return results
    # a simple optimization to above would be to first check for the
    # smaller of the two arrays and to adjust loops for shortest
    # path.

    # Solution 2: Using generic set datatype and the O[1] `in` comparison
    results = [x for x in set(nums1) if x in set(nums2)]
    return results

    # Solution 3: Using built-in Python set intersection
    return list(set(nums1) & set(nums2))

    # Alternatives
    # If the arrays are sorted,
    ### set a pointer at the start of each array
    ### compare value at each pointer
    ### if same, append the value and advance both pointers until we find a different number
    ### if different, advance the pointer for the lower value
    ### repeat comparison until we get the pointers to the end of both arrays

