#!/usr/bin/env python3

# HackerRank : Statistics
# Day 5 : Poisson Distribution II

# Parameters
# ----------
# lam_A {float}     average repair rate for machine A
# lam_B {float}     average repair rate for machine B
# 
# Returns
# -------
# exp_cost_A {float}    expected cost of repairs for machine A
# exp_cost_B {float}    expected cost of repairs for machine B

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
#lam_A, lam_B = ((float(a), float(b)) for a, b in input().split())
lam_A, lam_B = 0.88, 1.55       ### COULDN'T GET THE IMPORT TO WORK, SO...

# Define cost functions for each machine
cost_A = lambda x: 160 + 40 * x**2
cost_B = lambda x: 128 + 40 * x**2

# Expected value requires some algebra...
# C_A = 160 + 40X^2, where X~Poisson(theta), E(X)=theta, and Var(X)=theta
# E(C_A) = E(160 + 40X^2)
#        + E(160) + E(40X^2)
#        = 160 + 40E(X^2)
# from the identity Var(X) = E(X^2) - (E(X))^2,
#                so E(X^2) = Var(X) + (E(X))^2
# and...
# E(C_A) = 160 + 40(Var(X) + (E(X))^2)
# substitute...
# E(C_A) = 160 + 40(theta + theta^2)
### HOW TO IMPLEMENT THIS USING THE ORIGINAL COST FUNCTION?
exp_cost_A = 160 + 40 * (lam_A + lam_A**2)
exp_cost_B = 128 + 40 * (lam_B + lam_B**2)
print(f'{exp_cost_A:.3f}')
print(f'{exp_cost_B:.3f}')

