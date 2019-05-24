#!/bin/python

### DEBUG: some unanswered questions regarding what this function should do
### 1. What is largest value / string length expected?
### 2. What should happen if input exceeds this limit?
### 3. What should happen in result exceeds this limit?
### 4. What should be returned for invalid input?
### 5. Can we make any assumptions about the validity of the input, or
###    do we need to check for this?
### 6. What should happen for an 'overflow' condition?


def add_binary_strings(str1, str2):
    """
    Add string representations of two binary numbers.

    Parameters:
        str1, str2      string of 0's and 1's representing a binary number

    Returns:
        string representation of the sum of the inputs
    """
    max_len = max(len(str1), len(str2)) + 1
    a, b = str1.zfill(max_len), str2.zfill(max_len)

    result = ''
    carry = 0
    for i in reversed(range(max_len)):
        tot = int(a[i]) + int(b[i]) + carry
        carry = 0
        if tot > 1:
            carry = 1
            tot =  tot % 2
        result += str(tot)

    ### DEBUG: not handling condition where we have a result that lengthens the string

    return result[::-1].lstrip('0')


def test_empty_strings():
    str1 = ''
    str2 = ''
    expected = ''
    result = add_binary_strings(str1, str2)
    assert result == expected


def test_one_empty_string():
    str1 = ''
    str2 = '101'
    expected = '101'
    result = add_binary_strings(str1, str2)
    assert result == expected


def test_all_ones():
    str1 = '1111'
    str2 = '1111'
    expected = '11110'
    result = add_binary_strings(str1, str2)
    assert result == expected


def test_large_values():
    str1 = '1' * 100
    str2 = '1'
    expected = '1' + '0' * 100


if __name__ == '__main__':
    str1 = '101'    # 5
    str2 = '110011' # 51
    print(f'Adding binary strings\n\t{str1}\n\t{str2}')
    print(add_binary_strings(str1, str2))

