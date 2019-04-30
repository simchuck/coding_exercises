# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        """
        Check if occurence of words in a string matches specified pattern.

        parameters:
            pattern     str     single character pattern
            str         [str]   list of strings to be checked

        returns:
                        bool    True if list of strings matches the pattern
                                False if match fails
        """
        words = str.split()

        # return if invalid input (different number of items)
        if len(words) != len(pattern): return False

        # return if different numbers of distinct patterns/words
        if len(set(words)) != len(set(pattern)): return False

        group = dict(zip(pattern, words))

        return all([group[k] == words[i] for i, k in enumerate(pattern)])


# Submission Detail
# 33 / 33 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 13.1 MB
