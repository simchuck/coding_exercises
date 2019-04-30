#!/bin/python

def add_binary_strings(str1, str2):
    """
    Add string representations of two binary numbers.

    Parameters:
        str1, str2      string of 0's and 1's representing a binary number

    Returns:
        string representation of the sum of the inputs
    """
    max_len = max(len(str1), len(str2))
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

    return result[::-1]


if __name__ == '__main__':
    str1 = '101'    # 5
    str2 = '110011' # 51
    print(f'Adding binary strings\n\t{str1}\n\t{str2}')
    print(add_binary_strings(str1, str2))

