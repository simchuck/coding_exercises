#!/usr/bin/env python3

# HackerRank : Statistics
# Day 1 : Quartiles

# Parameters
# ----------
# _ {int}       number of elements
# N {array}     list of numbers
# 
# Returns
# -------
# Q1 {float}    1st quartile (25%)
# Q2 {float}    2nd quartile (50%)
# Q3 {float}    3rd quartile (75%)

from statistics import mean

# Get input
_ = int(input())
N = [int(n) for n in input().split()]

# Make sure it is sorted
X = sorted(X)

# Split the list of numbers and return with the median value
def split_numbers(N):
    L = len(N)
    lft, rgt = N[:L//2], N[(L+2)//2:]
    med = mean(N[(L-1)//2:L//2+1]
    return lft, med, rgt

# Get quartiles for the list
lft, Q2, rgt = split_numbers(X)
_, Q1, _ = split_numbers(lft)
_, Q3, _ = split_numbers(rgt)

print(f'{Q1:.1f}')
print(f'{Q2:.1f}')
print(f'{Q3:.1f}')
