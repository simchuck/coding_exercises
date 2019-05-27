#!/usr/bin/env python3

# HackerRank : Statistics
# Day 4 : Binomial Distribution

# Parameters
# ----------
# b {float}     ratio of boys to girls
# g {float}     normalized number of girls
# 
# Returns
# -------
# P {float}     cumulative probability for >= 3 successes

# Need the factorial function to calculate combinations
from math import factorial as F

# Define function for binomial distribution
def binomial(n, x, p):
    return F(n) / (F(n - x) * F(x)) * p**x * q**(n-x)

# Get input (as a space-delimited string of boy girl ratio)
b, g = (float(x) for x in input().split())

# Calculate probability for success (p) and failure (q)
p = b / (b + g)
q = 1 - p

# Set (fixed) parameters for the problem
n = 6
x = 3

# Determine cumulative probability for selecting at least 3 boys out of 6
P = sum([binomial(n, i, p) for i in range(3, n)])
print(f'{P:.3f}')

### DEBUG code to calculate probability for each individual outcome
#for x in range(1, n+1):
#    print(f'n: {x}: {binomial(n, x, p):.3f}')

