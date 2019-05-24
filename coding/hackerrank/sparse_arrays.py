#!/bin/python3
# https://www.hackerrank.com/challenges/sparse-arrays/problem

"""
There is a collection of input strings and a collection of query strings. For
each query string, determine how many times it occurs in the list of input
strings.

For example, given input `strings = ['ab', ' ab', ' abc']` and `queries = ['ab', ' abc', ' bc']`, we find 2 instances of `ab`, 1 of `abc` and 0 of `bc`. For each query, we add an element to our return array, `results = [2, 1, 0]`.

Function Description

Complete the function `matchingStrings` in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

`matchingStrings` has the following parameters:

    `strings` - an array of strings to search
    `queries` - an array of query strings

Input Format

The first line contains and integer `n`, the size of `strings`.
Each of the next `n` lines contains a string `strings[i]`.
The next line contains `q`, the size of `queries`.
Each of the next `q` lines contains a string `q[i]`.

Constraints

1 <= n <= 1000
1 <= q <= 1000
1 <= | strings[i], queries[i] | <= 20

Output Format

Return an integer array of the results of all queries in order.
"""

sample_input_1 = """
4
aba
baba
aba
xzxb
3
aba
xzxb
ab
"""

sample_output_1 = """
2
1
0
"""

sample_input_2 = """
3
def
de
fgh
3
de
lmn
fgh
"""

sample_output_2 = """
1
0
1
"""

sample_input_3 = """
13
abcde
sdaklfj
asdjf
na
basdn
sdaklfj
asdjf
na
asdjf
na
basdn
sdaklfj
asdjf
5
abcde
sdaklfj
asdjf
na
basdn
"""

sample_output_3 = """
1
3
4
3
2
"""

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
