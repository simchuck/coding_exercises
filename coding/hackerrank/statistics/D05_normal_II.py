#!/usr/bin/env python3

# HackerRank : Statistics
# Day 5 : Normal Distribution II

# Parameters
# ----------
# mu {float}        mean of the normal distribution
# stddev {float}    standard deviation of the normal distribution
# B_limit {float}   lower limit for a B grade
# F_limit {float}   lower limit for a passing grade
# 
# Returns
# -------
# {float}    probability of getting a B or better
# {float}    probability of getting a passing grade
# {float}    probability of getting a failing grade

# Need pi, sqrt, exp, and erf functions from the math module
import math

# Get input values.
mu, stddev = (float(x) for x in input().split())
B_limit    = float(input())
F_limit    = float(input())

# Probability density function for standard normal distribution
pdf = lambda x: math.exp(-x**2 / 2) / math.sqrt(2 * math.pi)
# Normal distribution function
normal = lambda x: (1 / stddev) * pdf((x - mu)/stddev)
# Cumulative distribution function for normal distribution
cdf = lambda x: 0.5 * (1 + math.erf((x - mu) / (stddev * math.sqrt(2))))

### ALTERNATE FUNCTION DEFINITIONS
#def pdf(x):
#    return math.exp(-x**2 / 2) / math.sqrt(2 * math.pi)
#def normal(mu, stddev, x):
#    return (1 / stddev) * pdf((x - mu)/stddev)
#def cdf(mu, stddev, x):
#    return 0.5 * (1 + math.erf((x - mu) / (stddev * math.sqrt(2))))

P_uptoB = 100 * cdf(B_limit)
# Probability that grade is >= 80
print(f'{100 - P_uptoB:.2f}')

P_fail = 100 * cdf(F_limit)
# Probability of passing grade (>= 60)
print(f'{100 - P_fail:.2f}')

# Probability of failing grade (< 60)
print(f'{P_fail:.2f}')

