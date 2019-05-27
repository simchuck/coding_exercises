#!/usr/bin/env python3

# HackerRank : Statistics
# Day 4 : Geometric Distribution II

# Parameters
# ----------
# num {int}     number of defects
# den {int}     number of samples per one defect
# n {int}       number of inspections over which defect might be found
# 
# Returns
# -------
# P {float}     probability of observing defect during n inspections

# Need the factorial function to calculate combinations
from math import factorial as F

def binomial(n, x, p):
    """
    Binomial distribution.
    
    Probability of x successes observed over n trials, with probability of
    success for each trial of p.
    """
    return F(n) / (F(n - x) * F(x)) * p**x * q**(n-x)

def nbinomial(n, x, p):
    """
    Negative binomial distribution.
    
    Probability of xth successful observation on the nth trial, with 
    probability of success for each trial of p.
    """
    return F(n - 1) / (F(n - 1 - (x - 1)) * F(x - 1)) * p**x * q**(n-x)

def geometric(n, p):
    """
    Geometric distribution.

    Probability of success observed on nth trial, with probability of 
    success for each trial of p.
    """
    return p * q**(n-1)

# Get input
num, den = (int(x) for x in input().split())
n = int(input())

# Calculate probability for finding a defect (p) 
p = float(num / den)
q = 1 - p

# Use geometric distribution for probability of first defect within n samples
P = sum([geometric(i, p) for i in range(1, n+1)])
print(f'{P:.3f}')

