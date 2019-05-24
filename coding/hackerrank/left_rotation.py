#!/bin/python3
# https://www.hackerrank.com/challenges/array-left-rotation/problem

import math
import os
import random
import re
import sys

def rotate_left(array, d):
    """
    Rotate a list to the left by specified number of spaces.

    A left rotation operation on an array of size `n` shifts each of the array's
    elements 1 unit to the left. For example, if 2 left rotations are performed
    on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 20].

    Given an array of `n` integers and a number, `d`, perform `d` left rotations
    on the array. Then print the updated array as a single line of space-separated
    integers.

    Input Format

    The first line contains two space-separated integers denoting the respective
    values of `n` (the number of integers) and `d` (the number of left rotations
    you must perform).
    The second line contains `n` space-separated integers describing the respective
    elements of the array's initial state.

    Constraints

    1 <= n <= 10**5
    1 <= d <= n
    1 <= a_i <= 10**6

    Output Format

    Print a single line of `n` space-separated integers denoting the final state
    of the array after performing left rotations.
    """
    if d == 0: return array

    # Using the deque object from the collections library
    #from collections import deque
    #array = deque(array)
    #array = list(array.rotate(-d))
    #return array

    # Using list methods to pop and append from ends of the list
    for i in range(d):
        array.append(array.pop(0))
    return array


if __name__ == '__main__':

    # First line of input gives number of integers and number of left rotations
    n, d = map(int, input().split())

    # Remaining line give list of itegers in the array
    a = list(map(int, input().rstrip().split()))

    test_simple_example


def test_simple_example():
    n = 5
    d = 4
    array = list(map(int, '1 2 3 4 5'.split()))

    expected = list(map(int, '5 1 2 3 4'.split()))

    result = rotate_left(array, d)

    assert result == expected
