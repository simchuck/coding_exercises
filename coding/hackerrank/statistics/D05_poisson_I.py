#!/usr/bin/env python3

# HackerRank : Statistics
# Day 5 : Poisson Distribution I

# Parameters
# ----------
# lam {float}    average, mean, rate of success
# k {int}           actual number of successes observed
# 
# Returns
# -------
# P {float}         probability of observing k successful outcomes

# Need the factorial function to calculate combinations
from math import factorial as F
# Need the exponent function for Poisson probability
from math import exp

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

def poisson(k, lam):
    """
    Poisson distribution.

    Probability of k successful observations given a rate of success lam.
    """
    return lam**k * exp(-lam) / F(k)

# Get input
lam = float(input())
k = int(input())

# Use Poisson distribution for probability k successes
P = poisson(k, lam)
print(f'{P:.3f}')

