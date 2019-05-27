#!/usr/bin/env python3

# HackerRank : Statistics
# Day 6 : Central Limit Theorem III

# The Central Limit Theorem states that for a large enough sample, the 
# distribution of the sample mean will approach a normal distribution.  

# Parameters
# ----------
# sample_size {int}     sample size
# avg_sample {float}    average of population
# std_sample (float}    standard deviation of population
# dist_range {float}    confidence interval (two-sided) for the sample
# z_score {float}       z-score corresponding to the confidence interval
# 
# Returns
# -------
# lower {float}         lower limit for the sample range
# upper {float}         upper limit for the sample range

# Need pi, sqrt, exp, and erf functions from the math module
import math

# Get input values.
sample_size     = int(input())
avg_population  = float(input())
std_population  = float(input())
dist_range      = float(input())
z_score         = float(input())

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

### I AM GETTING CONFUSED HERE - DIFFERENCE BETWEEN SAMPLE AND POPULATION...
### FOLLOWING IS INCOMPLETE (2018.01.12)
mu  = sample_size * avg_population
std = math.sqrt(sample_size) * std_population

# AS a first guess, we note that approximately 95% of the population falls
# between two standard deviations on either side of the mean for a normal
# distribution.  
B = mu + 2 * std
# The 'z-score' represents the normalized x-value for the distribution
# z = (x - mu) / std
x = z_score * std + mu

while P = 
P_enough_tix = cdf(mu, std, num_tix_available)
print(f'{P_enough_tix:.2f}')

