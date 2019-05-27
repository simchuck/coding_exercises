#!/usr/bin/env python3

# HackerRank : Statistics
# Day 4 : Binomial Distribution II

# Parameters
# ----------
# p {float}     probability of rejecting piston
# n {float}     number of pistons in a batch
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
p, n = (int(x) for x in input().split())

# Calculate probability for failure (q)
p = p / 100
q = 1 - p

# Set (fixed) parameters for the problem
x = 2

# Determine cumulative probability for no more than 2 rejects
P = sum([binomial(n, i, p) for i in range(0, x+1)])     # 0, 1, or 2 rejects
print(f'{P:.3f}')

# Determine cumulative probability for at least 2 rejects
P = sum([binomial(n, i, p) for i in range(x, n+1)])     # 2, 3, ... or n rejects
print(f'{P:.3f}')

### DEBUG code to calculate probability for each individual outcome
#for x in range(1, n+1):
#    print(f'n: {x}: {binomial(n, x, p):.3f}')

