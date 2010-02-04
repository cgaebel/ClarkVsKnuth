# Python 3.0. Why? Because I can!

# What was I trying to do with this? In my twisted naive mind,
# I thought to myself: "Wait, asymptotic notation ignores coefficients, right?
# well therefore, log_3(n) is faster than log_2(n). What if we took the
# standard exponentiation by squaring and cubed instead of squared. Surely
# that would be asymptotically faster! [log_2(n) vs. 2log_3(n)]

# This script is what I used to prove I'm an idiot.
# Note to self: Do the math next time - and realize how to change log bases.

import time
import math

mults = 0

def LinearPower(base, exponent):
    global mults
    
    result = base

    if exponent == 0:
        return 1

    for i in range(1, exponent):
        result *= base

    mults += exponent - 1

    return result

# Calculates base^exponent, with an interesting running
# time of: (logBase-1)log_logBase(exponent)
def Exponentiate(base, exponent, logBase):
    global mults
    
    if exponent < 2:
        if exponent == 1:
            return base
        if exponent == 0:
            return 1

    if (exponent % logBase) == 0:
        return LinearPower(Exponentiate(base, exponent/logBase, logBase), logBase)
    else:
        mults += 1
        return Exponentiate(base, exponent - 1, logBase) * base

# returns who won the round. Negative if I won, positive if Knuth won.
def RunComparisons(exponent):
    global mults
    
    mults = 0
    Exponentiate(2, exponent, 2)
    knuthsResult = mults
    #print("[2^", exponent, " - Knuth]: ", knuthsResult, sep='')

    mults = 0
    Exponentiate(2, exponent, 3)
    clarksResult = mults
    #print("[2^", exponent, " - Clark]: ", clarksResult, sep
    return knuthsResult - clarksResult

myTotalWins = 0
clarksWins = 0
knuthsWins = 0
ties = 0

iterations = 10000 # Adjust this in relation to your paranoia level.

# This loop checks for all values of n up to -iterations- to see which algorithm is better.
# If, at any value of n my algorithm works better than knuths, my total wins get incremented.
for i in range(iterations):
    result = RunComparisons(i)
    if result < 0:
        knuthsWins += 1
    elif result > 0:
        clarksWins += 1
    else:
        ties += 1

    if clarksWins > knuthsWins:
        myTotalWins += 1

print("Total wins: ", myTotalWins, "/", iterations, ".", " (", (myTotalWins/iterations) * 100, "%)", sep='')
