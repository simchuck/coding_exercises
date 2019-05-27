#!/usr/bin/env python3

# HackerRank : Statistics
# Day 5 : Normal Distribution I

# Parameters
# ----------
# mu {float}        mean of the normal distribution
# stddev {float}    standard deviation of the normal distribution
# lessthan {float}  upper limit for hours to manufacture
# low {float}       lower limit for manufacture time interval
# high {float}      upper limit for manufacture time interval
# 
# Returns
# -------
# {float}    probability that manufacture time is less than `lessthan`
# {float}    probability that manufacture time is between `low` and `high`

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

# Probability that a car can be assembled in less than `lessthan` hours.
print(f'{cdf(lessthan):.3f}')

# Probability that car assembly time will be between `low` and `high` hours.
print(f'{cdf(high) - cdf(low):.3f}')

