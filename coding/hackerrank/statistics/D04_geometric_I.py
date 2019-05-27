#!/usr/bin/env python3

# HackerRank : Statistics
# Day 4 : Geometric Distribution 

# Parameters
# ----------
# num {int}     number of defects
# den {int}     number of samples per one defect
# n {int}       sample when first defect is found
# 
# Returns
# -------
# P {float}     probability of observing defect on nth inspection

# Need the factorial function to calculate combinations
from math import factorial as F

def binomial(n, x, p):
    """Binomial distribution."""
    return F(n) / (F(n - x) * F(x)) * p**x * q**(n-x)

def nbinomial(n, x, p):
    """Negative binomial distribution."""
    return F(n - 1) / (F(n - 1 - (x - 1)) * F(x - 1)) * p**x * q**(n-x)

def geometric(n, p):
    """Geometric distribution."""
    return p * q**(n-1)

# Get input
num, den = (int(x) for x in input().split())
n = int(input())

# Calculate probability for finding a defect (p) 
p = float(num / den)
q = 1 - p

# Use geometric distribution for probability of first defect on nth sample
P = geometric(n, p)
print(f'{P:.3f}')

