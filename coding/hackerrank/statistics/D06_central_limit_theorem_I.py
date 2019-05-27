#!/usr/bin/env python3

# HackerRank : Statistics
# Day 6 : Central Limit Theorem I

# The Central Limit Theorem states that for a large enough sample, the 
# distribution of the sample mean will approach a normal distribution.  

# Parameters
# ----------
# max_capacity {float}      maximum capacity of the elevator
# num_boxes {int}           number of boxes
# avg_box_weight {float}    average weight per box
# std_box_weight (float}    standard deviation of box weight
# 
# Returns
# -------
# {float}    probability that weight of `num_boxes` is <= `max_capacity'

# Need pi, sqrt, exp, and erf functions from the math module
import math

# Get input values.
max_capacity   = float(input())
num_boxes      = int(input())
avg_box_weight = float(input())
std_box_weight = float(input())

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
# times the standard devaiation of each sample value.
mu  = num_boxes * avg_box_weight
std = math.sqrt(num_boxes) * std_box_weight

P_boxes_lte_capacity = cdf(mu, std, max_capacity)
print(f'{P_boxes_lte_capacity:.4f}')

