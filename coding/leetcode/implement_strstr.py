#!/bin/bash
# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Check for edge cases
        if not needle: return 0
        #if not haystack: return -1

        # Solution #1 (36ms, 13.1MB)
        # Using built-in python functions
        #return haystack.find(needle)

        # Solution #2 (36ms, 13.4MB)
        # Check from left until the item is found
        i = 0
        offset = len(needle)

        while i <= len(haystack) - offset:
            if haystack[i:i+offset] == needle:
                return i
            i += 1

        return -1
