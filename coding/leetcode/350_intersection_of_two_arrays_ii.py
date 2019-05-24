"""
Leetcode: 350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.
Each element in the result should appear as many times as it shows in both arrays.

https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""
from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:

    # Solution 1: Naive approach with nested for loop.
    # Need to advance pointers after each found element.
    results = []
	...
    return results
    # a simple optimization to above might be to first check for the
    # smaller of the two arrays and to adjust loops for shortest
    # path.

    # Solution 2: Assuming the arrays are sorted.
    # This makes the problem easier, since we can compare by matching indices.
    results = []
    for a, b in zip(nums1, nums2):
        if a == b: results.append(a)
    return results

    # Solution 2a: same thing but using a list comprehension
    results = [a for a, b in zip(nums1, nums2) if a == b]
    return results

    # Solution 3: Using python dict data type.
    ### loop through first list and create an dict key for each item, with
    ### a




