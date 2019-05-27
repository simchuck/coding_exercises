#!/usr/bin/env python3

# HackerRank : Statistics
# Day 6 : Central Limit Theorem II

# The Central Limit Theorem states that for a large enough sample, the 
# distribution of the sample mean will approach a normal distribution.  

# Parameters
# ----------
# num_tix_available {int}   number of tickets available for purchase
# num_students {int}        number of students buying tickets
# avg_tix_purchased {float} average number of tickets purchased
# std_tix_purchased (float} standard deviation of tickets purchased
# 
# Returns
# -------
# {float}    probability that all students can purchase their tickets

# Need pi, sqrt, exp, and erf functions from the math module
import math

# Get input values.
num_tix_available = int(input())
num_students      = int(input())
avg_tix_purchased = float(input())
std_tix_purchased = float(input())

# Probability density function for standard normal distribution
#pdf = lambda x: math.exp(-x**2 / 2) / math.sqrt(2 * math.pi)
def pdf(x):
    return math.exp(-x**2 / 2) / math.sqrt(2 * math.pi)
# Normal distribution function
#normal = lambda x: (1 / stddev) * pdf((x - mu)/stddev)
def normal(mu, stddev, x):
    return (1 / stddev) * pdf((x - mu)/stddev)
# Cumulative distribution function for normal distribution
#cdf = lambda x: 0.5 * (1 + math.erf((x - mu) / (stddev * math.sqrt(2))))
def cdf(mu, stddev, x):
    return 0.5 * (1 + math.erf((x - mu) / (stddev * math.sqrt(2))))

# For sufficiently large sample size (typical n >= 20 ???), the distribution
# of samples will approximate a normal distribution with sample mean equal to
# n times the mean of each sample value, and standard deviation of sqrt(n)
# times the standard deviation of each sample value.
mu  = num_students * avg_tix_purchased
std = math.sqrt(num_students) * std_tix_purchased

P_enough_tix = cdf(mu, std, num_tix_available)
print(f'{P_enough_tix:.4f}')

