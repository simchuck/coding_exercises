#!/usr/bin/env python3

# HackerRank : Statistics
# Day 1 : Interquartile Range

# Parameters
# ----------
# _ {int}       number of elements
# N {array}     list of numbers
# F {array}     frequency of each element
# 
# Returns
# -------
# IQR {float}   interquartile range

from statistics import mean

# Get input
_ = int(input())
N = [int(n) for n in input().split()]
F = [int(f) for f in input().split()]

# Construct the full array and make sure it is sorted
X = []
for n, f in zip(N, F):
    for _ in range(f):
        X.append(n)
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

# Calculate interquartile range
IQR = Q3 - Q1

print(f'{IQR:.1f}')
