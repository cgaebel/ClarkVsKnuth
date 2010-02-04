# Python 3.0. Why? Because I can!

# What was I trying to do with this? In my twisted naive mind,
# I thought to myself: "Wait, asymptotic notation ignores coefficients, right?
# well therefore, log_3(n) is faster than log_2(n). What if we took the
# standard exponentiation by squaring and cubed instead of squared. Surely
# that would be asymptotically faster! [log_2(n) vs. 2log_3(n)]

# This script is what I used to prove I'm an idiot.
# Note to self: Do the math next time.

import time
import math

def LinearPower(base, exponent):
    result = base

    if exponent == 0:
        return 1

    for i in range(1, exponent):
        result *= base

    return result

# Calculates base^exponent, with an interesting running
# time of: (logBase-1)log_logBase(exponent)
def Exponentiate(base, exponent, logBase):
    if exponent < 2:
        if exponent == 1:
            return base
        if exponent == 0:
            return 1

    if (exponent % logBase) == 0:
        return LinearPower(Exponentiate(base, exponent/logBase, logBase), logBase)
    else:
        return Exponentiate(base, exponent - 1, logBase) * base

####
